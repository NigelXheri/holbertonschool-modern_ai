#!/usr/bin/env python3
"""Scrape one product detail page with Selenium."""
import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Return the title, price, full description, and integer star count."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(delay)
        headings = driver.find_elements('css selector', '.caption h4')
        price = driver.find_element('css selector', 'h4.price')
        description = driver.find_element('css selector', 'p.description')
        stars = driver.find_elements('css selector',
                                     '.ratings .ws-icon.ws-icon-star')
        return {
            'title': headings[1].text,
            'price': price.text,
            'description': description.text,
            'rating': len(stars),
        }
    finally:
        driver.quit()
