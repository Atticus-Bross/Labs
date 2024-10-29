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
    test:dict=defaultdict(list)
    add_to_index('as',test)
    assert test=={'a':['as'],'s':['as'],'as':['as']}
    add_to_index('tas', test)
    assert test=={'a':['as','tas'],'s':['as','tas'],'as':['as','tas'],'t':['tas'],'ta':['tas'],'tas':['tas']}
def test_build_index()->None:
    """test_build_index()
    Tests the build_index function"""
    assert build_index(['a'])=={'a':['a']}
    assert build_index(['as','tas'])=={'a':['as','tas'],'s':['as','tas'],'as':['as','tas'],'t':['tas'],'ta':['tas'],'tas':['tas']}
    assert build_index(['a','as','tas'])=={'a':['a','as','tas'],'s':['as','tas'],'as':['as','tas'],'t':['tas'],'ta':['tas'],'tas':['tas']}
def test_fuzzy_pick()->None:
    """test_fuzzy_pick()
    Tests the fuzzy_pick function"""
    assert fuzzy_pick('the',{'a':['a','as','tas'],'s':['as','tas'],'as':['as','tas'],'t':['tas'],'ta':['tas'],'tas':['tas']})=={'tas':'t'}
    assert fuzzy_pick('sa',{'a':['a','as','tas'],'s':['as','tas'],'as':['as','tas'],'t':['tas'],'ta':['tas'],'tas':['tas']})=={'as':'s','tas':'s','a':'a'}
test_ngrams()
test_add_to_index()
test_build_index()
test_fuzzy_pick()