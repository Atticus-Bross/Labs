"""Test Lab B:

Module Testing the Lab B functions

Completed by Atticus Bross on 2024-11-22"""
from random import shuffle
from string import ascii_lowercase

from labb import *


def test_compare_symbol() -> None:
    """Tests the bubble_sort function"""
    assert compare_symbol(True) == '>'
    assert compare_symbol(False) == '<'
def test_bubble_sort() -> None:
    """Tests the bubble_sort function"""
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    test_list: list = [_ for _ in range(5)]
    for _ in range(5):
        shuffle(test_list)
        assert bubble_sort(test_list) == [0, 1, 2, 3, 4]
    for _ in range(5):
        shuffle(test_list)
        assert bubble_sort(test_list, True) == [4, 3, 2, 1, 0]
    test_list = [ascii_lowercase[index] for index in range(5)]
    for _ in range(5):
        shuffle(test_list)
        assert bubble_sort(test_list) == ['a', 'b', 'c', 'd', 'e']
    test_list: list = [float(_) for _ in range(5)]
    for _ in range(5):
        shuffle(test_list)
        assert bubble_sort(test_list) == [0.0, 1.0, 2.0, 3.0, 4.0]


def test_merge_sort() -> None:
    """Tests the merge_sort function"""
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1, 2, 3]) == [1, 2, 3]
    test_list: list = [_ for _ in range(5)]
    for _ in range(5):
        shuffle(test_list)
        assert merge_sort(test_list) == [0, 1, 2, 3, 4]
    for _ in range(5):
        shuffle(test_list)
        assert merge_sort(test_list, True) == [4, 3, 2, 1, 0]
    test_list = [ascii_lowercase[index] for index in range(5)]
    for _ in range(5):
        shuffle(test_list)
        assert merge_sort(test_list) == ['a', 'b', 'c', 'd', 'e']
    test_list: list = [float(_) for _ in range(5)]
    for _ in range(5):
        shuffle(test_list)
        assert merge_sort(test_list) == [0.0, 1.0, 2.0, 3.0, 4.0]


test_compare_symbol()
test_bubble_sort()
test_merge_sort()
