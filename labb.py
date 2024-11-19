
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


import random
random.seed()

root = None

for item in {random.randint(0,100) for _ in range(20)}:
    if root is None:
        root = Node(item)
    else:
        root.insert(item)

print(root)

