"""Lab 7
Module implementing functions for:

Creating Tables
Viewing Tables
Creating Zipper Merges
Applying a Caesar Cypher to Text

Completed by Atticus Bross on 2024-10-22 for DS-1043"""
from types import NoneType,UnionType
from typing import Sequence,Any,IO
import os
def same_len_error(seq:list[list]|list[dict],error_txt:str)->None:
    """same_len_error(seq, error_txt)
    Raises a ValueError if the sequences within seq are not all the same length

    seq: the sequence of sequences
    error_txt: the text to display for the error"""
    lengths:list=list(map(len,seq))
    if lengths.count(lengths[0])!=len(lengths):
        raise ValueError(error_txt)
def fix(value):
    """fix(value)
    Reduces floats to two decimal places, all other values are ignored

    value: the value"""
    if isinstance(value,float):
        return round(value,2)
    else:
        return value
def columns(values:list,cols:int)->list[list]:
    """columns(values, cols)
    Breaks data into a given number of columns

    values: the values to be broken up
    cols: the number of columns"""
    col_len:int=len(values)//cols
    columns2:list=[]
    for i in range(cols):
        col:list=[]
        for j in range(col_len):
            col.append(values[i+j*cols])
        columns2.append(col)
    return columns2
def alignment(value)->str:
    """alignment(value)
    Determines the alignment a value should have in a table

    value: the value to align"""
    if isinstance(value,int|float) and not isinstance(value,bool):
        return 'right'
    elif isinstance(value,str|bool):
        return 'left'
    else:
        raise ValueError('value must be either int, float, bool, or str')
def none_str(value)->str:
    """non_str(value)
    Converts the value to a string, None converts to a blank string

    value: the value to convert"""
    if value is None:
        return ''
    else:
        return str(value)
def add_alignment(values:list[str],aligns:list[str])->list[str]:
    """add_alignment(values, aligns)
    Adds proper markdown alignment to a list of strings
    
    values: the strings to be given alignment
    aligns: should be made up of the strings 'left' and 'right'"""
    aligned:list=[]
    for index, value in enumerate(values):
        if aligns[index]=='left':
            aligned.append(f':{value}')
        elif aligns[index]=='right':
            aligned.append(f'{value}:')
        else:
            raise ValueError("aligns must be either 'left' or 'right'")
    return aligned
def max_width(seqs:Sequence[Sequence])->int:
    """max_width(seqs)
    Finds the largest sequence within a sequence

    seqs: the sequence of sequences"""
    lengths:'map'=map(len,seqs)
    return max(lengths)
def rows(values:list,rows2:int)->list[list]:
    """rows(values, rows2)
    Breaks data up into a given number of rows

    values: the data
    rows2: the number of rows"""
    row_len:int=len(values)//rows2
    return_rows:list=[]
    for i in range(rows2):
        return_rows.append(values[i*row_len:(i+1)*row_len])
    return return_rows
def table_row(values:list[str],widths:list[int],aligns:list[str])->str:
    """table_row(values, widths, aligns)
    Creates the string for a row in a Markdown table

    values: the values in the row
    widths: the width each column is to be in the final table
    aligns: the alignment of each element in the row"""
    elements:list=[]
    for index, value in enumerate(values):
        if aligns[index]=='left':
            elements.append(f'{value:<{widths[index]}}')
        elif aligns[index]=='right':
            elements.append(f'{value:>{widths[index]}}')
        else:
            raise ValueError("aligns must be either 'left' or 'right'")
    return f'|{'|'.join(elements)}|\n'
def table(values:list[str],aligns:list[str],cols:int)->list[str]:
    """table(values, aligns, cols)
    Creates a table from a list of values and alignments

    values: a list of the values
    aligns: the alignments for each column
    cols: the number of columns"""
    cols2:list=columns(values,cols)
    #the width must be at least 4 to accommodate the minimum column specification, '---:'
    widths:list=list(map(lambda x:max(max_width(x),4),cols2))
    rows2:list=rows(values,len(values)//cols)
    return_rows:list=[]
    for index, row2 in enumerate(rows2):
        #cols is also the length of each row
        return_rows.append(table_row(row2,widths,aligns))
    #add header formatting row
    header_row:list=[]
    for width in widths:
        header_row.append('-'*(width-1))
    #add the proper semicolons to the header row
    header_row:list=add_alignment(header_row,aligns)
    return_rows.insert(1,table_row(header_row,widths,['left','left','left','left']))
    return return_rows
def list_type(seq:list):
    """list_type(seq)
    Returns the second value in a list that is not None

    seq: the list"""
    for element in seq[1:]:
        if not isinstance(element,NoneType):
            return element
def deep_unpack(seq:Sequence[Sequence],ignores:type|UnionType=str)->list:
    """deep_unpack(seq, ignores=str)
    Unpacks a sequence of sequences into a single sequence

    seq: the sequence
    ignores: the types of sequences to ignore"""
    unpacked:list=[]
    for element in seq:
        if isinstance(element,Sequence) and not isinstance(element,ignores):
            #this is to avoid the infinite recursion that occurs because a string contains a string which contains a string, etc.
            if isinstance(element,str) and len(element)==1:
                unpacked.append(element)
            else:
                unpacked.extend(deep_unpack(element,ignores))
        else:
            unpacked.append(element)
    return unpacked
def align(cols:list[list])->list[str]:
    """align(cols)
    Determines the alignment for a list of columns

    cols: the columns (also lists)"""
    aligns: list = list(map(list_type, cols))
    aligns = list(map(alignment, aligns))
    return aligns
def table_from_list(header:list,data:list[list])->list[str]:
    """table_from_list(header, data)
    Creates a table from a header and data that are lists of values

    header: the headers
    data: the values of the table"""
    same_len_error(data,'all rows must be the same length')
    if len(header)!=len(data[0]):
        raise ValueError('there must be as many headers as there are columns')
    unpacked:list=[*header,*deep_unpack(data)]
    unpacked=list(map(fix,unpacked))
    cols:list=columns(unpacked,len(header))
    aligns:list=align(cols)
    pass_values:list=list(map(none_str,unpacked))
    return table(pass_values,aligns,len(header))
def table_from_dict(header:list|dict[Any:str],data:list[dict])->list[str]:
    """table_from_dict(header, data)
    Generates a Markdown table from a list of dictionaries

    header: either a list of keys for data or a dictionary that shares keys with data
    data: the list of dictionaries"""
    if isinstance(header,list):
        unpacked:list=header.copy()
    elif isinstance(header,dict):
        unpacked:list=list(header.values())
    else:
        raise ValueError('header must be a list or dictionary')
    for row in data:
        for key in header:
            unpacked.append(row.setdefault(key))
    cols:list=columns(unpacked,len(header))
    aligns:list=align(cols)
    unpacked=list(map(none_str,unpacked))
    return table(unpacked,aligns,len(header))
def create_table(header:list|dict,data:list[list|dict])->list[str]:
    """create_table(header, data)
    Creates a list of strings describing the rows of a Markdown table

    header: a list of headers
    data: a list of the data values"""
    data_type:type=type(data[0])
    if data_type==list:
        return table_from_list(header,data)
    elif data_type==dict:
        return table_from_dict(header,data)
def view_table(header:list|dict,data:list[list|dict],max_width:int=os.get_terminal_size(),file:IO|None=None)->None:
    """view_table(header, data, max_width=os.get_terminal_size(), file=None)
    Pretty prints a table to a stream

    header: the headers of the table
    data: the data in the table
    max_width: the maximum width of the table, default is the width of the terminal
    file: the stream to print to"""
    print_table:list=create_table(header,data)
    #create_table ensures all rows are the same length
    if len(print_table[0])>max_width:
        for row in print_table:
            values:list=row.split('|')
            remove_all(values,'\n')
            remove_all(values,'')