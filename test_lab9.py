"""Test Lab 9:

Tests the Lab 9 functions

Completed by Atticus Bross on 2024/11/09 for DS-1043"""
from lab9 import *
def test_ngrams()->None:
    """test_ngrams()
    Tests the ngrams function"""
    assert ngrams('as')==['as','a','s']
    assert ngrams('the')==['the','th','he','t','h','e']
    assert ngrams('a')==['a']
def test_add_to_index()->None:
    """test_add_to_index()
    Tests the add_to_index function"""
    test:dict={}
    add_to_index('as',test)
    assert test=={'as':['as','a','s']}
    add_to_index('the', test)
    assert test=={'as':['as','a','s'],'the':['the','th','he','t','h','e']}
    add_to_index('a', test)
    assert test=={'as':['as','a','s'],'the':['the','th','he','t','h','e'],'a':['a']}
def test_build_index()->None:
    """test_build_index()
    Tests the build_index function"""
    assert build_index(['a'])=={'a':['a']}
    assert build_index(['the','as'])=={'the':['the','th','he','t','h','e'],'as':['as','a','s']}
    assert build_index(['a','as','the'])=={'as':['as','a','s'],'the':['the','th','he','t','h','e'],'a':['a']}
test_ngrams()
test_add_to_index()
test_build_index()