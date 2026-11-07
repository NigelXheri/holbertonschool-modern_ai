#!/usr/bin/env python3
"""Scrape products from a static category page with Selenium."""
import time
from selenium import webdriver


def scrape_products(url):
    """Return unique products from url in the order they appear.

    Each product has a title, price, and description as strings, and
    a rating as an integer.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        products = []
        seen = set()
        for card in driver.find_elements('css selector', '.thumbnail'):
            title = card.find_element('css selector', 'a.title')
            price = card.find_element('css selector', 'h4.price')
            description = card.find_element('css selector', 'p.description')
            rating = card.find_element(
                'css selector', '.ratings p[data-rating]'
            )
            product = {
                'title': title.get_attribute('title'),
                'price': price.text,
                'description': description.text,
                'rating': int(rating.get_attribute('data-rating')),
            }
            key = tuple(product.values())
            if key not in seen:
                seen.add(key)
                products.append(product)
        return products
    finally:
        driver.quit()


# Keep the entry point used by the supplied driver script.
scrape_products_list = scrape_products
