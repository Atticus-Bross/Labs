"""Test Lab 7
Module Testing the Lab 7 functions

Completed by Atticus Bross on 2024-10-22 for DS-1043"""
from typing import Callable
def test_error(error_type:type,f:Callable)->None:
    """test_error()
    Tests if a function gives the correct error

    error_type: the type of error expected
    f: the function, should be specified as lambda x: f(desired parameters)"""
    try:
        f()
        assert False
    except error_type:
        pass