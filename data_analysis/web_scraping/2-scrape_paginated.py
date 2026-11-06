#!/usr/bin/env python3
"""Module for scraping paginated quotes from quotes.toscrape.com."""

import time
from urllib import parse
from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """
    Scrapes all pages of quotes from quotes.toscrape.com
    by following 'Next' links.

    Args:
        base_url (str): The URL of the first page to start scraping.

    Returns:
        list: A combined list of quote dictionaries from all pages.
    """
    all_quotes = []
    current_url = base_url

    while current_url:
        all_quotes.extend(scrape_basic(current_url))

        html = fetch_html(current_url)
        soup = BeautifulSoup(html, 'html.parser')
        next_li = soup.find('li', class_='next')

        if next_li and next_li.a:
            current_url = parse.urljoin(base_url, next_li.a.get('href'))
            time.sleep(1)
        else:
            current_url = None

    return all_quotes
