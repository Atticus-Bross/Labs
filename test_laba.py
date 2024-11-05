"""Test Lab A:

Module testing the Lab A functions

Completed by Atticus Bross on 2024-11-12 for DS-1043"""
from laba import *

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
test_save_state()
test_load_state()