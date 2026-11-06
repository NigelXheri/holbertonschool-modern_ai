#!/usr/bin/env python3
"""Fetches a web page and returns its HTML as text via fetch_html()"""
import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetches a web page and returns its HTML as text"""
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.content

    except Exception:
        return \
            '{} Client Error: Not Found for url: {}'.format(
                response.status_code, url)
