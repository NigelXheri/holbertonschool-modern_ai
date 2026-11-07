#!/usr/bin/env python3
"""Logs in to Quotes to Scrape and extracts quotes."""
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Returns quotes from the first page using an authenticated session."""
    with requests.Session() as session:
        login_page = session.get(login_url)
        login_page.raise_for_status()
        form = BeautifulSoup(login_page.text, 'html.parser')
        token = form.find('input', attrs={'name': 'csrf_token'})
        if token is None or not token.get('value'):
            raise ValueError('Login form is missing a CSRF token')

        response = session.post(login_url, data={
            'username': user,
            'password': pwd,
            'csrf_token': token['value'],
        })
        response.raise_for_status()
        result = BeautifulSoup(response.text, 'html.parser')
        if result.find('input', attrs={'name': 'csrf_token'}):
            raise ValueError('Login failed')

        page = session.get(urljoin(login_url, '/'))
        page.raise_for_status()

    soup = BeautifulSoup(page.text, 'html.parser')
    return [
        {
            'text': quote.find(class_='text').get_text(),
            'author': quote.find(class_='author').get_text(),
            'tags': [tag.get_text() for tag in quote.find_all(class_='tag')],
        }
        for quote in soup.find_all('div', class_='quote')
    ]
