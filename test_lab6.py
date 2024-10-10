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
    assert variance((1,1,1,1))==0
    assert variance((1,2,3,4,5))==2
    assert variance((7,9,5,3,11))==8
def test_replace()->None:
    """test_replace() Tests the replace function"""
    test_list:list=[0,2,2,0,2,0]
    replace(test_list,0,1)
    assert test_list==[1,2,2,1,2,1]
    test_list = [True,None,False,None,True]
    replace(test_list, None, 42)
    assert test_list == [True, 42, False, 42, True]
    test_list = [0,0,0,(1,2),(1,2)]
    replace(test_list, (1,2), 12)
    assert test_list == [0,0,0,12,12]
def test_query_county()->None:
    """test_query_county() Tests the query_county function"""
    #unpack the one string in the tuple before sending it to int
    assert query_county(data[0],lambda x: int(*x),None,'fips')==31039
    assert query_county(data[1],lambda x: x[0]+x[1],None,'name','state')=='lancaster countyNE'
    assert query_county(data[2],lambda x: x[0]-x[1],'noaa','prcp','snow')==5.5
    assert (query_county(data[3],lambda x: x[0]*x[1]-x[2],'age','0-4','5-9','10-14')
        ==-0.05740344015901054)
def test_temp_variance()->None:
    """test_variance() Tests the variance function"""
    assert temp_variance(data[0])==365.9050000000001
    assert temp_variance(data[1])==348.186875
    assert temp_variance(data[2])==332.0118749999999
def test_growth()->None:
    """test_growth() Tests the variance function"""
    assert growth(data[3])==-323
    assert growth(data[4])==-149
    assert growth(data[5])==-322
# def test_deadlyness()->None:
#     """test_deadlyness() Tests the deadlyness function"""
#     assert isclose(deadlyness(data[6]),5.095238095238095)
#     assert isclose(deadlyness(data[7]),0.47619047619047616)
#     assert isclose(deadlyness(data[8]),0.5238095238095238)
# test_fetch()
# test_variance()
test_replace()
# test_query_county()
# test_temp_variance()
# test_growth()
# test_deadlyness()
# test file writing functions
# with open('files for writing/test.md','w') as mdfile:
#test header
#     header('test',1,mdfile)
#     header('test', 3, mdfile)
#     header('test', 6, mdfile)