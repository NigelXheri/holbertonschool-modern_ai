#!/usr/bin/env python3
"""Fetches quote data from all the quotes' API pages"""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetches quote data from all the quotes' API pages"""

    quotes_list = []
    page_number = 1

    while True:
        url = "{}/api/quotes?page={}".format(base_url, page_number)
        html = json.loads(fetch_html(url))
        quotes = html['quotes']
        quotes_list.extend({'text': quote['text'],
                            'author': quote['author']['name'],
                            'tags': quote['tags']}
                           for quote in quotes)

        if not html['has_next']:
            return quotes_list
        page_number += 1


if __name__ == "__main__":
    scrape_via_api("https://quotes.toscrape.com")
