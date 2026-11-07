#!/usr/bin/env python3
"""Extracts quotes from embedded JSON-LD."""
import json
from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Returns quote text, author names, and tags from the page."""
    soup = BeautifulSoup(fetch_html(url), 'html.parser')
    quotes = []

    for script in soup.find_all('script', type='application/ld+json'):
        data = json.loads(script.get_text())
        objects = data if isinstance(data, list) else [data]
        for item in objects:
            if not isinstance(item, dict) or item.get('@type') != 'Quote':
                continue

            tags = item.get('keywords', [])
            if isinstance(tags, str):
                tags = [tag.strip() for tag in tags.split(',') if tag.strip()]

            quotes.append({
                'text': item.get('text'),
                'author': item.get('author', {}).get('name'),
                'tags': tags,
            })

    return quotes
