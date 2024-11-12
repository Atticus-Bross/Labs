"""Test Lab A:

Module testing the Lab A functions

Completed by Atticus Bross on 2024-11-12 for DS-1043"""
from typing import Callable

from laba import *

START:str = urljoin(DOMAIN, '/index.html')
EXAMPLE1:str = get(START).text
EXAMPLE2:str = get('https://books.toscrape.com/catalogue/category/books/travel_2/index.html').text
EXAMPLE3: str = get('https://books.toscrape.com/catalogue/the-secret-garden_413/index.html').text
EXAMPLE4: str = get(
    'https://books.toscrape.com/catalogue/the-torch-is-passed-a-harding-family-story_945/index.html').text
EXAMPLE5: str = get(
    'https://books.toscrape.com/catalogue/foolproof-preserving-a-guide-to-small-batch-jams-jellies-pickles-condiments-and-more-a-foolproof-guide-to-making-small-batch-jams-jellies-pickles-condiments-and-more_978/index.html').text
SOUP3: Soup = Soup(EXAMPLE3, 'html.parser')
SOUP4: Soup = Soup(EXAMPLE4, 'html.parser')
SOUP5: Soup = Soup(EXAMPLE5, 'html.parser')
TABLE3: element.Tag = SOUP3.find('table')
TABLE4: element.Tag = SOUP4.find('table')
TABLE5: element.Tag = SOUP5.find('table')
def test_error(error_type: type, f: Callable) -> None:
    """Tests if a function gives the correct error

    error_type: the type of error expected
    f: the function, should be specified as lambda: f(desired parameters)"""
    try:
        f()
        assert False
    except error_type:
        pass
def test_save_state()->None:
    """Tests the save_state function"""
    save_state('test.json',['abc','efg'],{'a':{},'b':{}})
    with open('test.json','r') as jsonfile:
        assert json.load(jsonfile) == [['abc','efg'],{'a':{},'b':{}}]
    save_state('test.json', ['abc'], {'a': {}})
    with open('test.json', 'r') as jsonfile:
        assert json.load(jsonfile) == [['abc'], {'a': {}}]
    save_state('test.json', [], {})
    with open('test.json', 'r') as jsonfile:
        assert json.load(jsonfile) == [[], {}]
    save_state('test.json', ['abc', 'efg'], {'a': {1:2,3:4}, 'b': {},'c':{1:2}})
    with open('test.json', 'r') as jsonfile:
        assert json.load(jsonfile) == [['abc', 'efg'], {'a': {'1':2,'3':4}, 'b': {},'c':{'1':2}}]
def test_load_state()->None:
    """Tests the save_state function"""
    save_state('test.json',['abc','efg'],{'a':{},'b':{}})
    assert load_state('test.json') == (['abc','efg'],{'a':{},'b':{}})
    save_state('test.json', ['abc'], {'a': {}})
    assert load_state('test.json') == (['abc'], {'a': {}})
    save_state('test.json', [], {})
    assert load_state('test.json') == ([], {})
    save_state('test.json', ['abc', 'efg'], {'a': {1:2,3:4}, 'b': {},'c':{1:2}})
    assert load_state('test.json') == (['abc', 'efg'], {'a': {'1':2,'3':4}, 'b': {},'c':{'1':2}})
def test_handle_link()->None:
    """Tests the handle_link function"""
    test_error(TimeoutError,lambda:handle_link([urljoin(START,'/asd')],1))
    assert handle_link([START])==(START, Soup(EXAMPLE1,'html.parser'))
    assert handle_link([START,'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'])==('https://books.toscrape.com/catalogue/category/books/travel_2/index.html',Soup(EXAMPLE2,'html.parser'))
    assert handle_link(['https://books.toscrape.com/catalogue/category/books/travel_2/index.html',START])==(START,Soup(EXAMPLE1,'html.parser'))


def test_rows() -> None:
    """Tests the rows function"""
    assert rows([1, 2], 1) == [[1, 2]]
    assert rows([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert rows([1, 2, 3, 4, 5, 6], 3) == [[1, 2], [3, 4], [5, 6]]
    assert rows([1, 2, 3, 4, 5, 6], 2) == [[1, 2, 3], [4, 5, 6]]


def test_extract_table() -> None:
    """Tests the extract_table function"""
    assert extract_table(TABLE3)[:3] == [['UPC', 'abbb492978ff656d'], ['Product Type', 'Books'],
                                         ['Price (excl. tax)', '£15.08']]
    assert extract_table(TABLE4)[4:7] == [['Tax', '£0.00'], ['Availability', 'In stock (16 available)'],
                                          ['Number of reviews', '0']]
    assert extract_table(TABLE5)[3] == ['Price (incl. tax)', '£30.52']


test_save_state()
test_load_state()
test_handle_link()
test_rows()
test_extract_table()
