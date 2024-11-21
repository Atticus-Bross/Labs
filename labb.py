from typing import Sequence, Self
class Node:
    """A node for use in a binary search tree"""

    def __init__(self, value, parent: Self | None = None) -> None:
        self._parent: Self = parent
        self._left: None | Self = None
        self._right: None | Self = None
        self._value = value
        self._quantity: int = 1

    def __repr__(self) -> str:
        if self._left is None and self._right is None:
            return f'{self._value}'
        return f'{self._value} ({self._left}, {self._right})'

    def __eq__(self, other) -> bool:
        return self._value == other

    def __gt__(self, other) -> bool:
        return self._value > other

    def __lt__(self, other) -> bool:
        return self._value < other

    def __le__(self, other) -> bool:
        return self._value <= other

    def __ge__(self, other) -> bool:
        return self._value >= other

    def insert(self, value) -> None:
        """Inserts a value into the node network

        value: the value"""
        if value < self:
            if self._left is None:
                self._left = Node(value, self)
            else:
                self._left.insert(value)
        elif value > self:
            if self._right is None:
                self._right = Node(value, self)
            else:
                self._right.insert(value)
        elif value :
            self._quantity = self._quantity + 1


class Tree:
    """A binary search tree"""

    def __init__(self, iterable: Sequence = ()) -> None:
        if len(iterable) > 0:
            self._root: Node = Node(iterable[0])
            for value in iterable[1:]:
                self._root.insert(value)

    def insert(self, value) -> None:
        """Inserts a value into the tree

        value: the value to insert"""
        if hasattr(self, '_root'):
            self._root.insert(value)
        else:
            self._root = Node(value)

    def __iter__(self):
        yield from self._root.traverse()
def compare_symbol(isreversed: bool) -> str:
    """Determines the comparison symbol to use based on whether the sequence is reversed
    
    isreversed: whether the sequence is reversed"""
    if isreversed:
        compare = '>='
    else:
        compare = '<='
    return compare
def bubble_sort(data: list, reverse: bool = False) -> list:
    """Sorts a list by swapping out of order pairs

    data: the list to be sorted
    reverse: the list is sorted from least to greatest if reverse is False and from greatest to least if reverse is true"""
    compare: str = compare_symbol(reverse)
    sort_list1: list = data.copy()
    sort_list2: list = data.copy()
    while True:
        # the list conversion is necessary as it is not possible to slice an enumerate object
        for index, value in list(enumerate(sort_list1))[:-1]:
            if not eval(f'value {compare} sort_list1[index+1]'):
                sort_list2.insert(index, sort_list2.pop(index + 1))
                break
        if sort_list1 == sort_list2:
            return sort_list2
        sort_list1 = sort_list2.copy()


def halves(seq: Sequence) -> list[Sequence]:
    """Splits a sequence in half
    
    seq: the sequence"""
    midpoint: int = ((len(seq) + 1) // 2)
    part1: Sequence = seq[:midpoint]
    part2: Sequence = seq[midpoint:]
    return [part1, part2]
def merge_sort(data: list, reverse=False) -> list:
    """Uses merge sort to sort a list

    list: the list to be sorted
    reverse: the list is sorted from least to greatest if reverse is False and from greatest to least if reverse is true"""
    if len(data) < 2:
        return data.copy()
    compare: str = compare_symbol(reverse)
    # midpoint is the middle index + 1
    part1, part2 = halves(data)
    # this is so the type hint system understands that parts 1 and 2 are lists
    assert isinstance(part1, list) and isinstance(part2, list)
    sort1: list = merge_sort(part1, reverse)
    sort2: list = merge_sort(part2, reverse)
    position: int = 0
    for value in sort1:
        try:
            while not eval(f'value {compare} sort2[position]'):
                position = position + 1
            sort2.insert(position, value)
            position = position + 1
        except IndexError:
            sort2.append(value)
    return sort2


def recursive_bisect(sorted_data: list, value, start_index: int, isreversed: bool) -> int:
    """The function that preforms the recursive part of bisect_search, this is so the user does not specify parameters
    that should only be used during recursion when calling bisect_search
    
    sorted_data: the sorted data, this is given either by the user or as a slice of a larger list given by a higher
        level of recursion
    value: the value to search for
    start_index: the starting index of the slice of the original list
    isreversed: whether the data is sorted in reversed order"""
    if len(sorted_data) == 0:
        return -1
    elif len(sorted_data) == 1:
        if sorted_data[0] == value:
            return start_index
        else:
            return -1
    start, end = halves(sorted_data)
    # this is so the type hint system understands that start and end are lists
    assert isinstance(start, list) and isinstance(end, list)
    recursive_start_index: int = (len(sorted_data) + 1) // 2
    if isreversed:
        compare1: str = '>='
        compare2: str = '<='
    else:
        compare2: str = '>='
        compare1: str = '<='
    if eval(f'value {compare1} start[-1]'):
        return recursive_bisect(start, value, start_index, isreversed)
    elif eval(f'value {compare2} end[0]'):
        return recursive_bisect(end, value, start_index + recursive_start_index, isreversed)
    else:
        return -1

def bisect_search(sorted_data: list, value) -> int:
    """Searches a list of presorted data and gives the index of the value, or -1 if the value is not present

    sorted_data: the data to search
    value: the value to search for"""
    if len(sorted_data) == 0:
        return -1
    isreversed: bool = sorted_data[0] > sorted_data[-1]
    return recursive_bisect(sorted_data, value, 0, isreversed)
