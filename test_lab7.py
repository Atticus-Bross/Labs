"""Test Lab 7
Module Testing the Lab 7 functions

Completed by Atticus Bross on 2024-10-22 for DS-1043"""
from typing import Callable
import io
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
    test_error(ValueError,lambda:alignment([True,]))
    assert alignment(2)=='right'
    assert alignment(2.345)=='right'
    assert alignment('test')=='left'
    assert alignment(True)=='left'
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
    assert deep_unpack([[(1, 2, 3), ('abc', 'efg')], ['abc']], tuple|str) == [(1, 2, 3), ('abc', 'efg'), 'abc']
def test_align()->None:
    """test_align()
    Tests the align function"""
    assert align([['asdf',1,2,3],])==['right']
    assert align([['asdf','as','bc'],['sdf',None,3.4]])==['left','right']
    assert align([['asdf',None,None,None,1]])==['right']
def test_table_from_list()->None:
    """test_table_from_list()
    Tests the errors for the table_from_list function"""
    test_error(ValueError,lambda:table_from_list(['test','test'],[[1,2],[2,3,5]]))
    test_error(ValueError,lambda:table_from_list(['test','test'],[[1,2,3],[4,5,6]]))
def test_table_from_dict()->None:
    """test_table_from_dict()
    Tests the errors for the table_from_dict function"""
    test_error(ValueError,lambda:table_from_dict(('test','tes'),[{'test':0,'tes':1}]))
def test_prepare_row()->None:
    """test_prepare_row()
    Tests the prepare_row function"""
    assert prepare_row('|a|b|c|d|\n')==['|a','|b','|c','|d']
    assert prepare_row('|a|\n')==['|a',]
    assert prepare_row('|a|b|c|\n')==['|a','|b','|c']
def test_remove_cols()->None:
    """test_remove_cols()
    Tests the remove_cols function"""
    assert remove_cols('|a|b|c|\n',3)=='...'
    assert remove_cols('|a|\n',1)=='...'
    assert remove_cols('|a|b|c|\n',1)=='|a|b...'
    assert remove_cols('|a|b|c|d|\n',2)=='|a|b...'
def test_table_data()->None:
    """test_table_data()
    Tests the table_data function"""
    assert table_data(['Test','tester',1,'a',None,'b'],2)==(['Test','tester','1','a','','b'],['right','left'],2)
    assert table_data(['Test', 'tester', 1.234, True, 1.3751, False], 2) == (
    ['Test', 'tester', '1.23', 'True', '1.38', 'False'], ['right', 'left'], 2)
    assert table_data(['test',1,2,3,4],1)==(['test','1','2','3','4'],['right',],1)
def test_view_table()->None:
    """test_view_table()
    Tests the table_data function"""
    with io.StringIO() as test_output:
        view_table({10: 'Biiiiiig', True: 'test', 'a': 'square', 2.2: 'ccc'},
                   [{'a': 34, True: 'asd', 2.2: False, 10: 2.34534}, ], 25,test_output)
        assert test_output.getvalue()=="""|Biiiiiig|test|square...
|-------:|:---|-----:...
|    2.35|asd |    34...\n"""
    with io.StringIO() as test_output:
        view_table([0,True,2.3433,'abcde'],[{0:10},{True:14},{2.3433:15,'abcde':4}],80,test_output)
        assert test_output.getvalue()=="""|   0|True|2.34|abcde|
|---:|---:|---:|----:|
|  10|    |    |     |
|    |  14|    |     |
|    |    |  15|    4|\n"""
    with io.StringIO() as test_output:
        view_table([0, True, 2.3433, 'abcde'], [{0: 10}, {True: 14}, {2.3433: 15, 'abcde': 4}], 15, test_output)
        assert test_output.getvalue() == """|   0|True...
|---:|---:...
|  10|    ...
|    |  14...
|    |    ...\n"""
    with io.StringIO() as test_output:
        view_table({10:'Biiiiiig',True:'test','a':'square',2.2:'ccc'},[{'a':34,True:'asd',2.2:False,10:2.34534}],20,test_output)
        assert test_output.getvalue()=="""|Biiiiiig|test...
|-------:|:---...
|    2.35|asd ...\n"""
def test_merge_sorted_lists()->None:
    """test_merge_sorted_lists()
    Tests the merge_sorted_lists function"""
    assert merge_sorted_lists([1,2,3],[4,5,6],[7,8,9])==[1,4,7,2,5,8,3,6,9]
    assert merge_sorted_lists([1,2,3,4])==[1,2,3,4]
    assert merge_sorted_lists([1,],[1,2,3],[1,2,3,5])==[1,1,1]
    assert merge_sorted_lists([1,2],[3,4,5,6])==[1,3,2,4]
def test_caesar()->None:
    """test_caesar()
    Tests the caesar function"""
    assert caesar(ascii_lowercase+ascii_uppercase)=='nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    assert caesar(ascii_lowercase+ascii_uppercase,13)=='nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    assert caesar('tesr',1)=='ufts'
    assert caesar('Testing Caesar',5)=='Yjxynsl Hfjxfw'
    assert caesar('bA%yU^&R4t',25)=='aZ%xT^&Q4s'
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
test_align()
test_table_from_list()
test_table_from_dict()
test_table_data()
test_prepare_row()
test_remove_cols()
test_view_table()
test_merge_sorted_lists()
test_caesar()
#create a Markdown file to test some functions
function_to_test:str='table_from_dict'
with open('test.md','w') as mdfile:
    if function_to_test=='table':
        mdfile.writelines(table(['a','a','ab','abc'],['left','right'],2))
        mdfile.writelines(table(['a','ab','abc','abcd','abcde','abcdef','as','asd','asdf'],['right','left','left'],3))
        mdfile.writelines(table(['a','b','ab','bc','abc','bcd','abcd','bcde'],['left','right','right','left'],2))
    elif function_to_test=='table_from_list':
        mdfile.writelines(table_from_list(['test','tester','te'],[[None,None,None],[1,'a',1.23456],[1,'b',3.5677]]))
        mdfile.writelines(
            table_from_list([True, 'tester', 'te'], [[1.2341892402, 'asdfkjls;dhfl', 334578937], [1.24332, 'a', None], [1.345, None, 3]]))
        mdfile.writelines(
            table_from_list(['t', 't', 't','boolsbools'], [ [1, 'a', 1.23456,False],[None, None, None,None], [1, 'b', 3.5677,True]]))
    elif function_to_test=='table_from_dict':
        mdfile.writelines(table_from_dict([0,True,2.3433,'abcde'],[{0:10},{True:14},{2.3433:15,'abcde':4}]))
        mdfile.writelines(table_from_dict([0, True, 2.3433, 'abcde'], [{2.3433:8,'abcde':'asd'}, {0:True,True:2.345}, {0:False,True:23.345,2.3433:5,'abcde':'fgh'}]))
        mdfile.writelines(table_from_dict([0, True, 2.3433, 'abcde'], [{2.3433:8,'abcde':15651615615}, {0:True,True:2.345}, {0:False,True:23.345,2.3433:5,'abcde':0}]))
        mdfile.writelines(table_from_dict({10:'Biiiiiig',True:'test','a':'square',2.2:'ccc'},[{'a':34,True:'asd',2.2:False,10:2.34534}]))
        mdfile.writelines(table_from_dict({10: 'Biiiiiig', True: 'test', 'a': 'square', 2.2: 'ccc'},
                                          [{'a': 34, True: 'asd', 2.2: False, 10: 2.34534},{2.2:True,}]))
    elif function_to_test=='create_table':
        mdfile.writelines(create_table([0,True,2.3433,'abcde'],[{0:10},{True:14},{2.3433:15,'abcde':4}]))
        mdfile.writelines(
            create_table(['test', 'tester', 'te'], [[None, None, None], [1, 'a', 1.23456], [1, 'b', 3.5677]]))