#!/usr/bin/env python3
"""Fetches quote data from all the quotes' API pages"""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetches quote data from all the quotes' API pages"""

    quotes_list = []
    html = json.loads(fetch_html(base_url+"/api/quotes?page=1"))
    has_next = html.get('has_next')
    page_number = 1

    while has_next is not False:
        html = json.loads(fetch_html(base_url+"/api/quotes?page="
                                     + str(page_number)))
        quotes = html['quotes']
        quotes_list.extend({'text': quote['text'],
                            'author': quote['author']['name'],
                            'tags': quote['tags']}
                           for quote in quotes)

        page_number += 1
        has_next = html.get('has_next')
    print(quotes_list)
    print("\nEND OF QUOTES")


if __name__ == "__main__":
    scrape_via_api("https://quotes.toscrape.com")
