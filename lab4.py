"""Lab 4
Module implementing very basic statistics and probability functions.

Completed by Atticus Bross on 2024-09-17 for DS-1043"""
from random import randint, seed

Number = int | float
Sequence = list | tuple


def min(numbers: Sequence) -> Number | None:
    """Returns the minimum value of a sequence of numbers"""
    minimum: Number | None = None
    for number in numbers:
        if minimum is None or minimum > number:
            minimum = number
    return minimum


def max(numbers: Sequence) -> Number | None:
    """Returns the maximum value of a sequence of numbers"""
    maximum: Number | None = None
    for number in numbers:
        if maximum is None or maximum < number:
            maximum = number
    return maximum


def sum(numbers: Sequence) -> Number | None:
    """Returns the sum of a sequence"""
    sum2: Number | None = None
    for number in numbers:
        if sum2 is None:
            sum2 = number
        else:
            sum2 = sum2 + number
    return sum2


def average(numbers: Sequence) -> Number | None:
    """Returns the average of a sequence"""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def median(numbers: Sequence) -> Number | None:
    """Returns the median of a sequence"""
    if len(numbers) == 0:
        return None
    sorted_numbers = sorted(numbers)
    if len(numbers) % 2 == 1:
        middle: int = (len(numbers) + 1) // 2
        middle_index: int = middle - 1
        return sorted_numbers[middle_index]
    elif len(numbers) % 2 == 0:
        lower_middle: int = (len(numbers) + 1) // 2
        upper_middle: int = (len(numbers) + 1) // 2 + 1
        lower_middle_index: int = lower_middle - 1
        upper_middle_index: int = upper_middle - 1
        return (sorted_numbers[upper_middle_index] + sorted_numbers[lower_middle_index]) / 2


def mode(numbers: Sequence) -> Number | None:
    counts: dict = {}
    # create a dictionary mapping every number to how often it occurs
    for number in numbers:
        if number in counts.keys():
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1
    mode2: number | None = None
    for number in counts.keys():
        if mode2 is None or counts[mode2] < counts[number]:
            mode2 = number
    return mode2


def roll_dice(number: int, faces: int) -> tuple[int, ...]:
    rolls: tuple = ()
    for i in range(number):
        rolls = rolls + (randint(1, faces),)
    return rolls


seed()
