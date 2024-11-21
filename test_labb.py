"""Test Lab B:

Module Testing the Lab B functions

Completed by Atticus Bross on 2024-11-22"""
from random import shuffle, randint
from string import ascii_lowercase

from labb import *


def test_node_iter() -> None:
    """Tests the iteration of the Node class"""
    test_node: Node = Node(5)
    assert [value for value in test_node] == [5]
    test_node.insert(5)
    assert [value for value in test_node] == [5, 5]
    test_node.insert(3)
    assert [value for value in test_node] == [3, 5, 5]
    test_node.insert(2)
    assert [value for value in test_node] == [2, 3, 5, 5]
    test_node.insert(4)
    assert [value for value in test_node] == [2, 3, 4, 5, 5]
    test_node.insert(6)
    assert [value for value in test_node] == [2, 3, 4, 5, 5, 6]
    test_node.insert(6)
    assert [value for value in test_node] == [2, 3, 4, 5, 5, 6, 6]


def test_node_reverse() -> None:
    """Tests the reversion of the Node class"""
    test_node: Node = Node(5)
    assert [value for value in reversed(test_node)] == [5]
    test_node.insert(5)
    assert [value for value in reversed(test_node)] == [5, 5]
    test_node.insert(3)
    assert [value for value in reversed(test_node)] == [5, 5, 3]
    test_node.insert(2)
    assert [value for value in reversed(test_node)] == [5, 5, 3, 2]
    test_node.insert(4)
    assert [value for value in reversed(test_node)] == [5, 5, 4, 3, 2]
    test_node.insert(6)
    assert [value for value in reversed(test_node)] == [6, 5, 5, 4, 3, 2]
    test_node.insert(6)
    assert [value for value in reversed(test_node)] == [6, 6, 5, 5, 4, 3, 2]
def test_tree() -> None:
    """Tests the initialization of the Tree class"""
    test_tree2: Tree = Tree()
    assert hasattr(test_tree2, '_root') is False
    test_tree2 = Tree([1])
    assert test_tree2._root == 1
    assert test_tree2._root._left is None
    assert test_tree2._root._right is None
    test_tree2 = Tree([1, 2])
    assert test_tree2._root == 1
    assert test_tree2._root._left is None
    assert test_tree2._root._right is not None
    assert test_tree2._root._right == 2
    test_tree2 = Tree([2, 1, 3])
    assert test_tree2._root == 2
    assert test_tree2._root._left is not None
    assert test_tree2._root._left == 1
    assert test_tree2._root._right == 3


def test_tree_insert() -> None:
    """Tests the insert method of the Tree class"""
    test_tree2: Tree = Tree()
    test_tree2.insert(5)
    assert test_tree2._root == 5
    test_tree2.insert(3)
    assert test_tree2._root._left == 3
    test_tree2.insert(8)
    assert test_tree2._root._right == 8
    test_tree2.insert(3)
    assert test_tree2._root._left._quantity == 2
    test_tree2.insert(6)
    assert test_tree2._root._right._left == 6


def test_tree_iter():
    """Tests iteration for the Tree class"""
    test_tree2: Tree = Tree()
    test_tree2.insert(5)
    assert [value for value in test_tree2] == [5]
    test_tree2.insert(5)
    assert [value for value in test_tree2] == [5, 5]
    test_tree2.insert(3)
    assert [value for value in test_tree2] == [3, 5, 5]
    test_tree2.insert(2)
    assert [value for value in test_tree2] == [2, 3, 5, 5]
    test_tree2.insert(4)
    assert [value for value in test_tree2] == [2, 3, 4, 5, 5]
    test_tree2.insert(6)
    assert [value for value in test_tree2] == [2, 3, 4, 5, 5, 6]
    test_tree2.insert(6)
    assert [value for value in test_tree2] == [2, 3, 4, 5, 5, 6, 6]
def test_compare_symbol() -> None:
    """Tests the compare_symbol function"""
    assert compare_symbol(True) == '>='
    assert compare_symbol(False) == '<='
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
    test_list = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    for _ in range(5):
        shuffle(test_list)
        assert bubble_sort(test_list) == [1, 1, 1, 2, 2, 3, 3, 3, 3]


def test_halves() -> None:
    """Tests the halves function"""
    assert halves([]) == [[], []]
    assert halves([1]) == [[1], []]
    assert halves([1, 2]) == [[1], [2]]
    assert halves((1, 2)) == [(1,), (2,)]
    assert halves([3, 4, 1, 2]) == [[3, 4], [1, 2]]
    assert halves([6, 8, 3]) == [[6, 8], [3]]
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
    test_list = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    for _ in range(5):
        shuffle(test_list)
        assert merge_sort(test_list) == [1, 1, 1, 2, 2, 3, 3, 3, 3]

def test_recursive_bisect() -> None:
    """Tests the recursive_bisect function"""
    for _ in range(5):
        assert recursive_bisect([], randint(1, 5), 0, True) == -1
    assert recursive_bisect([4], 4, 0, True) == 0
    assert recursive_bisect([1, 2, 3, 4, 5, 6], 2, 0, False) == 1
    assert recursive_bisect([1, 2, 3], 2, 0, False) == 1
    assert recursive_bisect([6, 5, 4, 3, 2, 1], 2, 0, True) == 4
    assert recursive_bisect([1, 2, 3, 4], 2, 0, False) == 1
    assert recursive_bisect([1, 2, 3, 4], 3, 0, False) == 2
    for _ in range(5):
        assert recursive_bisect([1, 2, 3, 4, 5], randint(6, 10), 0, False) == -1
    assert recursive_bisect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 5, 0, False) == 4
def test_bisect_search() -> None:
    """Tests the bisect_search function"""
    for _ in range(5):
        assert bisect_search([], randint(1, 5)) == -1
    assert bisect_search([4], 4) == 0
    assert bisect_search([1, 2, 3, 4, 5, 6], 2) == 1
    assert bisect_search([1, 2, 3], 2) == 1
    assert bisect_search([6, 5, 4, 3, 2, 1], 2) == 4
    assert bisect_search([1, 2, 3, 4], 2) == 1
    assert bisect_search([1, 2, 3, 4], 3) == 2
    for _ in range(5):
        assert bisect_search([randint(1, 5) for _ in range(7)], randint(6, 10)) == -1


test_node_iter()
test_node_reverse()
test_tree()
test_tree_insert()
test_tree_iter()
test_compare_symbol()
test_bubble_sort()
test_halves()
test_merge_sort()
test_recursive_bisect()
test_bisect_search()
