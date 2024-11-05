""" Lab A: Web Scraping

Crawls the website http://books.toscrape.com and creates a spreadsheet of books.
"""
import time
import random
import requests
import json
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup as Soup

# User Agent from Chrome Browser on Win 10/11
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

DEFAULT_SLEEP = 3.0 # These may need tuning
SIGMA = 1.0

DOMAIN = 'http://books.toscrape.com' # Ideally, these would be
STATE_FILENAME = 'state.json'        # read in from a configuration
OUTPUT_FILENAME = 'books.csv'        # or commandline, but this is fine


def get(url: str) -> requests.Response:
    """Waits a random amount of time, then send a GET request"""
    time.sleep(random.gauss(DEFAULT_SLEEP, SIGMA))
    return requests.get(url, headers=HEADERS)


# [TODO] Save links left to visit and the data extracted to a JSON file
def save_state(filename: str, links: list[str], data: dict[str, dict]) -> None:
    pass


# [TODO] Load links left to visit and collected data from a JSON file
def load_state(filename: str) -> tuple[list[str], dict[str, dict]]:
    pass


# [TODO] Write all data to a CSV file
def write_spreadsheet(filename: str, data: dict[str, dict]) -> None:
    pass


if __name__ == '__main__':
    # [TODO] Load the state file or start fresh if it cannot be read
    to_visit: list = ['/index.html']
    data: dict[str, dict] = {}
    # Main Loop
    while len(to_visit) > 0:
        try:
            pass
            # [TODO] Process files from to_visit
            #        This requires:
            #        - Popping a link from the list
            #        - Checking to see if it has already been processed
            #        - Downloading the file the link points to
            #          - Link should not be removed from to_visit if it
            #            cannot be downloaded
            #        - Add the current file to data, using the url as the
            #          key, and a dictionary containing book data if present
            #        - Extract links from the HTML
            #          - Use urljoin(full_url_of_current_doc, link_ref)
            #            to create the full url for a link
            #          - Check to see if this full url is already in data
            #          - If not, append to to_visit
        except KeyboardInterrupt:
            save_state(STATE_FILENAME, to_visit, data)
            is_finished = False
            break
    else:
        is_finished = True
    if is_finished:
        write_spreadsheet(OUTPUT_FILENAME, data)
