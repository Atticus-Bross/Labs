"""Test Lab A:

Module testing the Lab A functions

Completed by Atticus Bross on 2024-11-12 for DS-1043"""
from laba import *
from typing import Callable
START:str = urljoin(DOMAIN, '/index.html')
EXAMPLE1:str = get(START).text
EXAMPLE2:str = get('https://books.toscrape.com/catalogue/category/books/travel_2/index.html').text
def test_error(error_type: type, f: Callable) -> None:
    """test_error()
    Tests if a function gives the correct error

    error_type: the type of error expected
    f: the function, should be specified as lambda: f(desired parameters)"""
    try:
        f()
        assert False
    except error_type:
        pass
def test_save_state()->None:
    """test_save_state()
    Tests the save_state function"""
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
    """test_save_state()
    Tests the save_state function"""
    save_state('test.json',['abc','efg'],{'a':{},'b':{}})
    assert load_state('test.json') == (['abc','efg'],{'a':{},'b':{}})
    save_state('test.json', ['abc'], {'a': {}})
    assert load_state('test.json') == (['abc'], {'a': {}})
    save_state('test.json', [], {})
    assert load_state('test.json') == ([], {})
    save_state('test.json', ['abc', 'efg'], {'a': {1:2,3:4}, 'b': {},'c':{1:2}})
    assert load_state('test.json') == (['abc', 'efg'], {'a': {'1':2,'3':4}, 'b': {},'c':{'1':2}})
def test_handle_link()->None:
    """test_handle_link()
    Tests the handle_link function"""
    test_error(TimeoutError,lambda:handle_link([urljoin(START,'/asd')],1))
    assert handle_link([START])==(START, Soup(EXAMPLE1,'html.parser'))
    assert handle_link([START,'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'])==('https://books.toscrape.com/catalogue/category/books/travel_2/index.html',Soup(EXAMPLE2,'html.parser'))
    assert handle_link(['https://books.toscrape.com/catalogue/category/books/travel_2/index.html',START])==(START,Soup(EXAMPLE1,'html.parser'))
test_save_state()
test_load_state()
test_handle_link()
