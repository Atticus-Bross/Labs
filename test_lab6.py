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
    assert variance({'a':7,'b':9,'c':5,'d':3,'e':11})==8
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
    test_list = [0, 0, 0]
    replace(test_list, (1, 2), 12)
    assert test_list == [0, 0, 0]
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
def test_deadlyness()->None:
    """test_deadlyness() Tests the deadlyness function"""
    assert isclose(deadlyness(data[6]),5.095238095238095)
    assert isclose(deadlyness(data[7]),0.47619047619047616)
    assert isclose(deadlyness(data[8]),0.5238095238095238)
def test_education()->None:
    """test_education() Tests the education function"""
    assert education(data[9])==22.4
    assert education(data[10]) == 20.7
    assert education(data[11]) == 25.0
def test_portion_female()->None:
    """test_portion_female() Tests the portion_female function"""
    assert isclose(portion_female(data[12]),0.5154362416107383)
    assert isclose(portion_female(data[13]), 0.5059422750424448)
    assert isclose(portion_female(data[14]), 0.5105024127164348)
def test_oldness()->None:
    """test_oldness() Tests the oldness function"""
    assert isclose(oldness(data[15]),0.15382452193475815)
    assert isclose(oldness(data[16]), 0.26166568222090963)
    assert isclose(oldness(data[17]), 0.19619293615587624)
def test_youngness()->None:
    """test_youngness() Tests the youngness function"""
    assert isclose(youngness(data[18]),0.26888371648120396)
    assert isclose(youngness(data[19]), 0.26092930302273293)
    assert isclose(youngness(data[20]), 0.2657428791377983)
def test_age_variance()->None:
    """test_age_variance() Tests the age_variance function"""
    assert isclose(age_variance(data[21]),0.0001782786942683424)
    assert isclose(age_variance(data[22]), 0.00011766529826546195)
    assert isclose(age_variance(data[23]), 0.00020695619312116284)
def test_employees()->None:
    """test_employees() Tests the age_variance function"""
    assert employees(data[24]['industry'])==(4,206,652,77,609,42,53,213,6,101,31,692,11,325,83)
    assert employees(data[25]['industry']) == (22, 254, 7, 265, 418, 174, 921, 379, 208, 44, 165, 27, 272, 9, 424\
        , 118, 365, 325, 4)
    assert employees(data[26]['industry']) == (58, 42, 137, 134, 67, 50, 18, 14, 249, 58, 59)
def test_raw_employment()->None:
    """test_raw_employment() Tests the raw_employment function"""
    assert isclose(raw_employment(fetch(data[24],'population','industry')),0.2881135752064582)
    assert isclose(raw_employment(fetch(data[25], 'population', 'industry')), 0.16766991770801584)
    assert isclose(raw_employment(fetch(data[26], 'population', 'industry')), 0.16995971609437943)
# test_fetch()
# test_variance()
# test_replace()
# test_query_county()
# test_temp_variance()
# test_growth()
# test_deadlyness()
# test_education()
# test_portion_female()
# test_oldness()
# test_youngness()
# test_age_variance()
# test_employees()
test_raw_employment()
# test file writing functions
# with open('files for writing/test.md','w') as mdfile:
#test header
#     header('test',1,mdfile)
#     header('test', 3, mdfile)
#     header('test', 6, mdfile)