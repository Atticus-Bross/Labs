"""Test of Lab 4
Module testing the Lab 4 functions.

Completed by Atticus Bross on 2024-09-17 for DS-1043"""
from lab4 import *


def test_empty_error() -> None:
    try:
        empty_error((), 'test')
        assert False
    except ValueError:
        pass


def test_min() -> None:
    """Tests the min function"""
    try:
        min(())
        assert False
    except ValueError:
        pass
    assert min((5,)) == 5
    assert min([5, ]) == 5
    assert min((3, 3)) == 3
    assert min([3, 3]) == 3
    assert min((3, 4, 7)) == 3
    assert min([3, 4, 7]) == 3


def test_max() -> None:
    """Tests the max function"""
    try:
        max(())
        assert False
    except ValueError:
        pass
    assert max((5,)) == 5
    assert max([5, ]) == 5
    assert max((3, 3)) == 3
    assert max([3, 3]) == 3
    assert max((3, 4, 7)) == 7
    assert max([3, 4, 7]) == 7


def test_sum() -> None:
    """Tests the sum function"""
    try:
        sum(())
        assert False
    except ValueError:
        pass
    assert sum((5,)) == 5
    assert sum([5, ]) == 5
    assert sum((3, 4, 7)) == 14
    assert sum([3, 4, 7]) == 14


def test_average() -> None:
    """Tests the average function"""
    try:
        average(())
        assert False
    except ValueError:
        pass
    assert sum((5,)) == 5
    assert sum([5, ]) == 5
    assert sum((3, 4, 7, 6)) == 20
    assert sum([3, 4, 7, 6]) == 20


def test_median() -> None:
    """Tests the median function"""
    try:
        median(())
        assert False
    except ValueError:
        pass
    assert median((1,)) == 1
    assert median([1, ]) == 1
    assert median((2, 3, 1)) == 2
    assert median([2, 3, 1]) == 2
    assert median((1, 7, 2, 4)) == 3
    assert median([1, 7, 2, 4]) == 3


def test_mode() -> None:
    """Tests the mode function"""
    try:
        mode(())
        assert False
    except ValueError:
        pass
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


test_empty_error()
test_min()
test_max()
test_sum()
test_average()
test_median()
test_mode()
test_roll_dice()
