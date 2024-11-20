
class Node:

    def __init__(self, value, parent=None):
        self._parent = parent
        self._left = None
        self._right = None
        self._value = value
        self._quantity = 1

    def __repr__(self):
        if self._left is None and self._right is None:
            return f'{self._value}'
        return f'{self._value} ({self._left}, {self._right})'

    def __eq__(self, other):
        return self._value == other

    def __gt__(self, other):
        return self._value > other

    def __lt__(self, other):
        return self._value < other

    def __le__(self, other):
        return self._value <= other

    def __ge__(self, other):
        return self._value >= other

    def insert(self, value):
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


def compare_symbol(isreversed: bool) -> str:
    """Determines the comparison symbol to use based on whether the sequence is reversed
    
    isreversed: whether the sequence is reversed"""
    if isreversed:
        compare = '>'
    else:
        compare = '<'
    return compare
def bubble_sort(data: list, reverse: bool = False) -> list:
    """Sorts a list by swapping out of order pairs

    data: the list to be sorted
    reverse: the list is sorted from least to greatest if reverse is False and from greatest to least if reverse is true"""
    compare: str = ''
    if reverse:
        compare = '>'
    elif not reverse:
        compare = '<'
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


def merge_sort(data: list, reverse=False) -> list:
    """Uses merge sort to sort a list

    list: the list to be sorted
    reverse: the list is sorted from least to greatest if reverse is False and from greatest to least if reverse is true"""
    if len(data) < 2:
        return data.copy()
    compare: str = ''
    if reverse:
        compare = '>'
    elif not reverse:
        compare = '<'
    # midpoint is the middle index + 1
    midpoint: int = ((len(data) + 1) // 2)
    part1: list = data[:midpoint]
    part2: list = data[midpoint:]
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


def bisect_search(sorted_data: list, value) -> int:
    """Searches a list of presorted data and gives the index of the value, or -1 if the value is not present

    sorted_data: the data to search
    value: the value to search for"""
    if len(sorted_data) == 0:
        return -1
    elif len(sorted_data) == 1:
        return 0
    isreversed: bool = sorted_data[0] > sorted_data[1]
    start, end = halves(sorted_data)
    if isreversed:
        if value >= start[-1]:
            return bisect_search(start, value)
        elif value <= end[0]:
            return bisect_search(end, value)
        else:
            return -1
    elif not isreversed:
        if value <= start[-1]:
            return bisect_search(start, value)
        elif value >= end[0]:
            return bisect_search(end, value)
        else:
            return -1
