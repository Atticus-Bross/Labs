from lab6 import *
def test_seq_comb()->None:
    """test_seq_com() Tests the seq_comb function"""
    assert seq_comb('abc',lambda x,y:x+y)==('ab','ac','bc')
    assert seq_comb((1,2,3),lambda x,y:x+y)==(3,4,5)
    assert seq_comb({'a':1,'b':2,'c':3},lambda x,y:x-y)==(-1,-2,-1)
    assert seq_comb([1,2,3],lambda x,y:x*y)==(2,3,6)
    assert seq_comb({'a':1,'b':1,'c':1},lambda x,y:x-y)==(0,0,0)
test_seq_comb()