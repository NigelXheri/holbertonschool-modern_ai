#!/usr/bin/env python3
"""Scrape a product category that loads more items on scroll."""
import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Return unique products, waiting up to scroll_pause per scroll."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        height = driver.execute_script('return document.body.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, arguments[0])', height)
            # Continue as soon as the next batch increases the page height.
            deadline = time.monotonic() + scroll_pause
            while True:
                new_height = driver.execute_script(
                    'return document.body.scrollHeight'
                )
                remaining = deadline - time.monotonic()
                if new_height > height or remaining <= 0:
                    break
                time.sleep(min(0.1, remaining))
            if new_height <= height:
                break
            height = new_height

        products = []
        seen = set()
        for card in driver.find_elements('css selector', 'div.thumbnail'):
            title = card.find_element('css selector', 'a.title')
            name = title.get_attribute('title')
            price = card.find_element('css selector', 'h4.price').text
            key = (name, price)
            if key in seen:
                continue
            seen.add(key)

            description = card.find_element('css selector', 'p.description')
            stars = card.find_elements('css selector',
                                       '.ratings .ws-icon.ws-icon-star')
            products.append({
                'title': name,
                'price': price,
                'description': description.text,
                'rating': len(stars),
            })
        return products
    finally:
        driver.quit()
