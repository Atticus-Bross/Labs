"""Test Lab 9:

Tests the Lab 9 functions

Completed by Atticus Bross on 2024/11/09 for DS-1043"""
from lab9 import *
def test_ngrams()->None:
    """test_ngrams()
    Tests the ngrams function"""
    assert ngrams('as')==['a','s','as']
    assert ngrams('the')==['t','h','e','th','he','the']
    assert ngrams('a')==['a']
test_ngrams()