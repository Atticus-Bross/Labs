"""Lab 7
Module implementing functions for:

Creating Tables
Viewing Tables
Creating Zipper Merges
Applying a Caesar Cypher to Text

Completed by Atticus Bross on 2024-10-22 for DS-1043"""
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
    Determines the alignment of a value should have in a table

    value: the value to align"""
    if isinstance(value,int|float) and not isinstance(value,bool):
        return 'right'
    else:
        return 'center'
def none_str(value)->str:
    """non_str(value)
    Converts the value to a string, None converts to a blank string

    value: the value to convert"""
    if value is None:
        return ''
    else:
        return str(value)
def table_from_list(header:list,data:list[list])->list[str]:
    """table_from_list(header, data)
    Creates a table from a header and data that are lists of values

    header: the headers
    data: the values of the table"""
    unpacked:list=[*header,*data]
    unpacked=list(map(fix,unpacked))
    col:list=columns(unpacked,len(header))
    #type of the elements within the columns, [1] is the first element that is not a header
    aligns:list=list(map(alignment,unpacked))
    # maps the lists within col
    pass_values:list=list(map(none_str,unpacked))
    table(pass_values,aligns)
def create_table(header:list|dict,data:list[list]|list[dict])->list[str]:
    """create_table(header, data)
    Creates a list of strings describing the rows of a Markdown table

    header: a list of headers
    data: a list of the data values"""
    same_len_error(data,'all rows must be the same length')
    data_type:type=type(data[0])
    #whether all the sequence in data are the same length has already been checked
    if data_type==list and len(header)!=len(data[0]):
        raise ValueError('there must be as many headers as there are columns')
    if data_type==list:
        return table_from_list(header,data)
    elif data_type==dict:
        return table_from_dict(header,data)