""" Lab A: Web Scraping

Crawls the website http://books.toscrape.com and creates a spreadsheet of books.

Completed by Atticus Bross on 2024-11-12 for DS-1043"""
import time
import random
import requests
import json
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup as Soup
from typing import Any

# User Agent from Chrome Browser on Win 10/11
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

DEFAULT_SLEEP = 1.0 # These may need tuning
SIGMA = 0.33

DOMAIN = 'http://books.toscrape.com' # Ideally, these would be
STATE_FILENAME = 'state.json'        # read in from a configuration
OUTPUT_FILENAME = 'books.csv'        # or commandline, but this is fine


def get(url: str) -> requests.Response:
    """Waits a random amount of time, then send a GET request"""
    time.sleep(random.gauss(DEFAULT_SLEEP, SIGMA))
    return requests.get(url, headers=HEADERS)


# [TODO] Save links left to visit and the data extracted to a JSON file
def save_state(filename: str, links: list[str], data2: dict[str, dict])-> None:
    """Saves links and data to a file

    filename: the name of the file
    links: a list of the links left to visit
    data: the data that has already been extracted"""
    with open(filename,'w') as jsonfile:
        json.dump((links,data2),jsonfile)


# [TODO] Load links left to visit and collected data from a JSON file
def load_state(filename: str) -> tuple[list[str], dict[str, dict]]:
    """Loads links and data from a file

    filename: the name of the file"""
    with open(filename,'r') as jsonfile:
        return tuple(json.load(jsonfile)) #type: ignore
def handle_link(links:list[str],timeout:int=60)->tuple[str,Soup]:
    """Handles loading the next link from to_visit

    links: the to_visit list
    timeout: the amount of time the function tries to do the download before raising a timeout error"""
    link2:str=links.pop()
    response:requests.Response=get(link2)
    #try until the download succeeds or a timeout occurs
    start:float = time.time()
    while not response.ok:
        response: requests.Response = get(link2)
        if time.time()-start>timeout:
            raise TimeoutError
    return link2,Soup(response.text,'html.parser')
def extract_data(raw_text:str)->dict[str,Any]:
    """Extracts the required data from a raw_text, this will be an empty dictionary if the data is not present

    raw_text: the text containing the data"""
# [TODO] Write all data to a CSV file
def write_spreadsheet(filename: str, data2: dict[str, dict]) -> None:
    pass


if __name__ == '__main__':
    # [TODO] Load the state file or start fresh if it cannot be read
    to_visit: list = [urljoin(DOMAIN,'/index.html')]
    data: dict[str, dict] = {}
    try:
        to_visit, data = load_state(STATE_FILENAME)
    except FileNotFoundError|ValueError:
        pass
    # Main Loop
    while len(to_visit) > 0:
        try:
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
            link, text = handle_link(to_visit)
            sub_data:dict = extract_data(text)
            data[link]=sub_data
            update(to_visit, text, data, link)
        except KeyboardInterrupt:
            save_state(STATE_FILENAME, to_visit, data)
            is_finished = False
            break
    else:
        is_finished = True
    if is_finished:
        write_spreadsheet(OUTPUT_FILENAME, data)
