
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
