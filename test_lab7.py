"""Test Lab 7
Module Testing the Lab 7 functions

Completed by Atticus Bross on 2024-10-22 for DS-1043"""
from typing import Callable

from lab7 import *


def test_error(error_type:type,f:Callable)->None:
    """test_error()
    Tests if a function gives the correct error

    error_type: the type of error expected
    f: the function, should be specified as lambda: f(desired parameters)"""
    try:
        f()
        assert False
    except error_type:
        pass
def test_same_len_error()->None:
    """test_same_len_error()
    Tests the same_len_error function"""
    same_len_error([[], [], []], '')
    same_len_error([[1,2],['a','b'],[True,False]],'')
    same_len_error([[1,], ['a',], [True,]], '')
    test_error(ValueError,lambda:same_len_error([[],[1]],''))
    test_error(ValueError,lambda:same_len_error([[1,2],[3,4,5]],''))
    test_error(ValueError, lambda: same_len_error([[1, 2,3,4], [3, 4, 5]], ''))
def test_fix()->None:
    """test_fix()
    Tests the fix function"""
    assert fix('a')=='a'
    assert fix(8.9058)==8.91
    assert fix(2.1)==2.1
def test_columns()->None:
    """test_columns()
    Tests the columns function"""
    assert columns([1,2,3,4],2)==[[1,3],[2,4]]
    assert columns([1,2,3,4,5,6],3)==[[1,4],[2,5],[3,6]]
    assert columns([1,2,3,4,5,6],2)==[[1,3,5],[2,4,6]]
def test_alignment()->None:
    """test_columns()
    Tests the alignment function"""
    test_error(ValueError,lambda:alignment(True))
    assert alignment(2)=='right'
    assert alignment(2.345)=='right'
    assert alignment('test')=='left'
def test_none_str()->None:
    """test_none_str()
    Tests the none_str function"""
    assert none_str(None)==''
    assert none_str(12)=='12'
    assert none_str(True)=='True'
    assert none_str('asd')=='asd'
def test_add_alignment()->None:
    """test_add_alignment()
    Tests the add_alignment function"""
    test_error(ValueError,lambda:add_alignment(['ad','bc'],['left','a']))
    assert add_alignment(['asd','bfc','ert'],['left','left','left'])==[':asd',':bfc',':ert']
    assert add_alignment(['abc', 'efg'], ['right', 'right']) == ['abc:','efg:']
    assert add_alignment(['word', 'test', 'cube','some'], ['left', 'right', 'left','right']) == [':word','test:',':cube','some:']
    assert add_alignment(['-','----','--','---'],['right','left','right','left'])==['-:',':----','--:',':---']
def test_max_width()->None:
    """test_max_width()
    Tests the max_width function"""
    assert max_width([[]])==0
    assert max_width([[],[],[]])==0
    assert max_width([[1,2],[3,4],[2,3]])==2
    assert max_width([[1,2,3]])==3
    assert max_width([[1,2],[1],[1,2,3],[3,4,5]])==3
def test_rows()->None:
    """test_rows()
    Tests the rows function"""
    assert rows([1,2],1)==[[1,2]]
    assert rows([1,2,3,4],2)==[[1,2],[3,4]]
    assert rows([1,2,3,4,5,6],3)==[[1,2],[3,4],[5,6]]
    assert rows([1,2,3,4,5,6],2)==[[1,2,3],[4,5,6]]
def test_table_row()->None:
    """test_table_row()
    Tests the table_row function"""
    assert table_row([':abc'],[7],['left'])=='|:abc   |\n'
    assert table_row(['abc:'], [6], ['right']) == '|  abc:|\n'
    assert table_row([':abc','efg:',':hij','lmn:'],[5,8,6,9],['left','right','left','right'])=='|:abc |    efg:|:hij  |     lmn:|\n'
def test_list_type()->None:
    """test_list_type()
    Tests the list_type function"""
    assert list_type([1,2,3,4,5])==2
    assert list_type([1.2,3.4,5.6])==3.4
    assert list_type(['a','b','c'])=='b'
    assert list_type(['test',1,2,3,4])==1
    assert list_type(['a',None,None,None,1.2])==1.2
def test_deep_unpack()->None:
    """test_deep_unpack()
    Tests the deep_unpack function"""
    assert deep_unpack([[None,'abc',1.2],[True,3],['ghf']])==[None,'abc',1.2,True,3,'ghf']
    assert deep_unpack([[['abc',None],[],2.34],[[],[True,3]]])==['abc',None,2.34,True,3]
    assert deep_unpack([[(1,2,3),('abc','efg')],['abc']],tuple)==[(1,2,3),('abc','efg'),'a','b','c']
test_same_len_error()
test_fix()
test_columns()
test_alignment()
test_none_str()
test_add_alignment()
test_max_width()
test_rows()
test_table_row()
test_list_type()
test_deep_unpack()
#create a Markdown file to test some functions
function_to_test:str='table_from_list'
with open('test.md','w') as mdfile:
    if function_to_test=='table':
        mdfile.writelines(table(['a','a','ab','abc'],['left','right'],2))
        mdfile.writelines(table(['a','ab','abc','abcd','abcde','abcdef','as','asd','asdf'],['right','left','left'],3))
        mdfile.writelines(table(['a','b','ab','bc','abc','bcd','abcd','bcde'],['left','right','right','left'],2))
    elif function_to_test=='table_from_list':
        mdfile.writelines(table_from_list(['test','tester','te'],[[None,None,None],[1,'a',1.23456],[1,'b',3.5677]]))