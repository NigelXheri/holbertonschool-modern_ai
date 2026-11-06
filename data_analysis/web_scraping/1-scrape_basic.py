#!/usr/bin/env python3
"""Scrapes the first page of quotes from quotes.toscrape.com."""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Scrapes the first page of quotes from quotes.toscrape.com."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    quotes = []
    quote_cards = soup.find_all("div", class_='quote')
    for quote in quote_cards:
        quote_dict = {'text': quote.span.get_text(),
                      'author': quote.find(class_='author').get_text(),
                      'tags': [tag.get_text()
                               for tag in quote.find_all(class_='tag')]}
        quotes.append(quote_dict)
    return quotes
