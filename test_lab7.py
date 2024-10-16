"""Test Lab 7
Module Testing the Lab 7 functions

Completed by Atticus Bross on 2024-10-22 for DS-1043"""
from typing import Callable

from lab7 import *


def test_error(error_type:type,f:Callable)->None:
    """test_error()
    Tests if a function gives the correct error

    error_type: the type of error expected
    f: the function, should be specified as lambda: f(desired parameters)"""
    try:
        f()
        assert False
    except error_type:
        pass
def test_same_len_error()->None:
    """test_same_len_error()
    Tests the same_len_error function"""
    same_len_error([[], [], []], '')
    same_len_error([[1,2],['a','b'],[True,False]],'')
    same_len_error([[1,], ['a',], [True,]], '')
    test_error(ValueError,lambda:same_len_error([[],[1]],''))
    test_error(ValueError,lambda:same_len_error([[1,2],[3,4,5]],''))
    test_error(ValueError, lambda: same_len_error([[1, 2,3,4], [3, 4, 5]], ''))
def test_fix()->None:
    """test_fix()
    Tests the fix function"""
    assert fix('a')=='a'
    assert fix(8.9058)==8.91
    assert fix(2.1)==2.1
def test_columns()->None:
    """test_columns()
    Tests the columns function"""
    assert columns([1,2,3,4],2)==[[1,3],[2,4]]
    assert columns([1,2,3,4,5,6],3)==[[1,4],[2,5],[3,6]]
    assert columns([1,2,3,4,5,6],2)==[[1,3,5],[2,4,6]]
def test_alignment()->None:
    """test_columns()
    Tests the alignment function"""
    assert alignment(2)=='right'
    assert alignment(2.345)=='right'
    assert alignment('test')=='center'
    assert alignment(True)=='center'
def test_none_str()->None:
    """test_none_str()
    Tests the none_str function"""
    assert none_str(None)==''
    assert none_str(12)=='12'
    assert none_str(True)=='True'
    assert none_str('asd')=='asd'
test_same_len_error()
test_fix()
test_columns()
test_alignment()
test_none_str()
