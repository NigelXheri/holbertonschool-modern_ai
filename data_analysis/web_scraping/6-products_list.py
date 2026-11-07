#!/usr/bin/env python3
"""Scrapes products from a static category page."""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_products(url):
    """Returns the products displayed on the given category page."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        products = []
        for card in driver.find_elements(By.CSS_SELECTOR, '.thumbnail'):
            title = card.find_element(By.CSS_SELECTOR, 'a.title')
            price = card.find_element(By.CSS_SELECTOR, 'h4.price')
            description = card.find_element(By.CSS_SELECTOR, 'p.description')
            rating = card.find_element(By.CSS_SELECTOR,
                                       '.ratings p[data-rating]')
            products.append({
                'title': title.get_attribute('title'),
                'price': price.text,
                'description': description.text,
                'rating': int(rating.get_attribute('data-rating')),
            })
        return products
    finally:
        driver.quit()


scrape_products_list = scrape_products
