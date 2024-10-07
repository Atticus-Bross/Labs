"""Test of Lab 4
Module testing the Lab 4 functions.

Completed by Atticus Bross on 2024-09-17 for DS-1043"""
from lab4 import *


def test_min() -> None:
    """Tests the min function"""
    assert min(()) is None
    assert min([]) is None
    assert min((5,)) == 5
    assert min([5, ]) == 5
    assert min((3, 3)) == 3
    assert min([3, 3]) == 3
    assert min((3, 4, 7)) == 3
    assert min([3, 4, 7]) == 3


def test_max() -> None:
    """Tests the max function"""
    assert max(()) is None
    assert max([]) is None
    assert max((5,)) == 5
    assert max([5, ]) == 5
    assert max((3, 3)) == 3
    assert max([3, 3]) == 3
    assert max((3, 4, 7)) == 7
    assert max([3, 4, 7]) == 7


def test_sum() -> None:
    """Tests the sum function"""
    assert sum(()) is None
    assert sum([]) is None
    assert sum((5,)) == 5
    assert sum([5, ]) == 5
    assert sum((3, 4, 7)) == 14
    assert sum([3, 4, 7]) == 14


def test_average() -> None:
    """Tests the average function"""
    assert sum(()) is None
    assert sum([]) is None
    assert sum((5,)) == 5
    assert sum([5, ]) == 5
    assert sum((3, 4, 7, 6)) == 20
    assert sum([3, 4, 7, 6]) == 20


def test_median() -> None:
    """Tests the median function"""
    assert median(()) is None
    assert median([]) is None
    assert median((1,)) == 1
    assert median([1, ]) == 1
    assert median((2, 3, 1)) == 2
    assert median([2, 3, 1]) == 2
    assert median((1, 7, 2, 4)) == 3
    assert median([1, 7, 2, 4]) == 3


def test_mode() -> None:
    """Tests the mode function"""
    assert mode(()) is None
    assert mode([]) is None
    assert mode((1,)) == 1
    assert mode([1, ]) == 1
    assert mode((0, 1, 0, 1, 0)) == 0
    assert mode([0, 1, 0, 1, 0]) == 0
    assert mode((0, 0, 1, 1, 1)) == 1
    assert mode([0, 0, 1, 1, 1]) == 1


def test_roll_dice() -> None:
    """Tests the roll_dice function"""
    assert roll_dice(1, 1) == (1,)
    assert roll_dice(3, 1) == (1, 1, 1)
    rolls: tuple[int, ...] = roll_dice(3, 3)
    assert len(rolls) == 3
    for roll in rolls:
        assert 1 <= roll <= 3


test_min()
test_max()
test_sum()
test_average()
test_median()
test_mode()
test_roll_dice()
