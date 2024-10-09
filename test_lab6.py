from lab6 import *
from math import isclose
def test_fetch()->None:
    """test_fetch() Tests the fetch function"""
    assert fetch('abc',0,1)==('a','b')
    assert fetch({1:2,3:4,5:6},3,5)==(4,6)
    assert fetch([1,2,3,4,5],0,2,4)==(1,3,5)
    assert fetch((1,2,3,4,5),1,3)==(2,4)
def test_variance()->None:
    """test_variance() Tests the variance function"""
    assert isclose(variance((1,1,1,1)),0)
    assert isclose(variance((1,2,3,4,5)),2)
    assert isclose(variance((7,9,5,3,11)),8)
# test_fetch()
test_variance()
#test file writing functions
# with open('files for writing/test.md','w') as mdfile:
#     header('test',1,mdfile)
#     header('test', 3, mdfile)
#     header('test', 6, mdfile)