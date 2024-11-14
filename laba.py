""" Lab A: Web Scraping

Scrapes the website http://books.toscrape.com and creates a spreadsheet of books.

Completed by Atticus Bross on 2024-11-12 for DS-1043"""

import csv
import json
import random
import time
from typing import Any, Iterable
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as Soup, element

# User Agent from Chrome Browser on Win 10/11
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

DEFAULT_SLEEP = 1.0  # These may need tuning
SIGMA = 0.33

DOMAIN = 'http://books.toscrape.com'  # Ideally, these would be
STATE_FILENAME = 'state.json'  # read in from a configuration
OUTPUT_FILENAME = 'books.csv'  # or commandline, but this is fine
TABLE_HEADERS: list = ['Title', 'Category', 'UPC', 'Product Type', 'Price (excl. tax)', 'Price (incl. tax)', 'Tax',
                       'Availability', 'Number of reviews']


def constrain(variable: int | float, min2: int | float, max2: int | float) -> int | float:
    """Constrains a variable to be within a minimum and maximum value"""
    return max(min(variable, max2), min2)


def get(url: str) -> requests.Response:
    """Waits a random amount of time, then send a GET request"""
    # the constrain function keeps sleep times within reason
    time.sleep(constrain(random.gauss(DEFAULT_SLEEP, SIGMA), 0.1, 2))
    return requests.get(url, headers=HEADERS)


def save_state(filename: str, links: list[str], data2: dict[str, dict]) -> None:
    """Saves links and data to a file

    filename: the name of the file
    links: a list of the links left to visit
    data: the data that has already been extracted"""
    with open(filename, 'w') as jsonfile:
        json.dump((links, data2), jsonfile)


def load_state(filename: str) -> tuple[list[str], dict[str, dict]]:
    """Loads links and data from a file

    filename: the name of the file"""
    with open(filename, 'r') as jsonfile:
        return tuple(json.load(jsonfile))  # type: ignore


def handle_link(links: list[str], timeout: int = 60) -> tuple[str, Soup]:
    """Handles loading the next link from to_visit

    links: the to_visit list
    timeout: the amount of time the function tries to do the download before raising a timeout error"""
    link2: str = links.pop()
    response: requests.Response = get(link2)
    # try until the download succeeds or a timeout occurs
    start: float = time.time()
    while not response.ok:
        response: requests.Response = get(link2)
        if time.time() - start > timeout:
            raise TimeoutError
    return link2, Soup(response.text, 'html.parser')


def rows(values: list, rows2: int) -> list[list]:
    """Breaks data up into a given number of rows

    values: the data
    rows2: the number of rows"""
    row_len: int = len(values) // rows2
    return_rows: list = []
    for i in range(rows2):
        return_rows.append(values[i * row_len:(i + 1) * row_len])
    return return_rows


def extract_table(table: element.Tag) -> list[list[str]]:
    """Extracts the data from an element.Tag table

    table: the raw table"""
    values: list[str] = [''.join(value.string.split('Â')) for value in table.find_all(['th', 'td'])]
    return rows(values, 7)


def extract_data(raw_text: Soup) -> dict[str, Any]:
    """Extracts the required data from a raw_text, this will be an empty dictionary if the data is not present

    raw_text: the text containing the data"""
    if raw_text.find(string='Product Description') is None:
        return {}
    title: str = raw_text.find('li', class_='active').string
    category: str = raw_text.find_all('a')[3].string
    raw_data: dict[str, Any] = {'Title': title, 'Category': category}
    table: element.Tag = raw_text.find('table')
    raw_data.update({header: value for header, value in extract_table(table)})
    return raw_data


def update(link2: str, to_visit2: list[str], data2: dict[str, dict[str, Any]], raw_text: Soup) -> None:
    """Updates to_visit with the new links

    link2: the URL of the current webpage
    to_visit2: the list of links to visit
    data2: the data already collected
    raw_text: a soup object of the data from the webpage"""
    links: Iterable[str | element.Tag] = raw_text.find_all('a')
    # extract the actual link from the element.Tag objects
    links = map(lambda x: x['href'], links)
    # filter out the internal links
    links = filter(lambda x: not x.startswith('#'), links)
    links = map(lambda x: urljoin(link2, x), links)
    visited: Iterable = data2.keys()
    links = filter(lambda x: x not in to_visit2 and x not in visited, links)
    to_visit2.extend(links)


def write_spreadsheet(filename: str, data2: dict[str, dict]) -> None:
    """Writes the data to a csv file"""
    if len(data2) < 1:
        raise ValueError('There must be at least one datapoint.')
    to_write: list = [data3 for data3 in data2.values() if len(data3) > 0]
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer: csv.DictWriter = csv.DictWriter(csvfile, TABLE_HEADERS)
        writer.writeheader()
        writer.writerows(to_write)


if __name__ == '__main__':
    to_visit: list = [urljoin(DOMAIN, '/index.html')]
    data: dict[str, dict] = {}
    try:
        to_visit, data = load_state(STATE_FILENAME)
    # the FileNotFoundError is for when there is no state file
    # the ValueError is for when the state file is blank
    except (FileNotFoundError, ValueError):
        pass
    # Main Loop
    while len(to_visit) > 0:
        try:
            link, soup = handle_link(to_visit)
            sub_data: dict = extract_data(soup)
            data[link] = sub_data
            update(link, to_visit, data, soup)
        except KeyboardInterrupt:
            save_state(STATE_FILENAME, to_visit, data)
            is_finished = False
            break
    else:
        is_finished = True
    if is_finished:
        write_spreadsheet(OUTPUT_FILENAME, data)
