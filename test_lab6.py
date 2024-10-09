from lab6 import *
from math import isclose
def test_seq_comb()->None:
    """test_seq_com() Tests the seq_comb function"""
    #if the function manages to execute an assertion error will be raised
    try:
        seq_comb((),lambda x:x)
        assert False
    except ValueError:
        pass
    try:
        seq_comb({1:2},lambda x:x)
        assert False
    except ValueError:
        pass
    assert seq_comb('abc',lambda x,y:x+y)==('ab','ac','bc')
    assert seq_comb((1,2,3),lambda x,y:x+y)==(3,4,5)
    assert seq_comb({'a':1,'b':2,'c':3},lambda x,y:x-y)==(-1,-2,-1)
    assert seq_comb([1,2,3],lambda x,y:x*y)==(2,3,6)
    assert seq_comb({'a':1,'b':1,'c':1},lambda x,y:x-y)==(0,0,0)
def test_fetch()->None:
    """test_fetch() Tests the fetch function"""
    assert fetch('abc',0,1)==('a','b')
    assert fetch({1:2,3:4,5:6},3,5)==(4,6)
    assert fetch([1,2,3,4,5],0,2,4)==(1,3,5)
    assert fetch((1,2,3,4,5),1,3)==(2,4)
def test_temp_variance()->None:
    """test_temp_variance() Tests the temp_variance function"""
    assert isclose(temp_variance(0),27.3)
    assert isclose(temp_variance(1),26.683333333333334)
    assert isclose(temp_variance(2),26.05)
# test_seq_comb()
# test_fetch()
# test_temp_variance()
#test file writing functions
with open('files for writing/test.md','w') as mdfile:
    header('test',1,mdfile)
    header('test', 3, mdfile)
    header('test', 6, mdfile)