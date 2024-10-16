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
def table_from_list(header:list,data:list[list])->list[str]:
    """table_from_list(header, data)
    Creates a table from a header and data that are lists of values

    header: the headers
    data: the values of the table"""
    fixed:'map'=map(fix,data)
    col:list=columns(header,fixed)
    #type of the elements within the columns
    col_types:'map'=map(lambda x:type(x[1]),col)
    aligns:'map'=map(alignment,col_types)
    widths:'map'=map(min_width,col)
    unpacked:list=extract(header,fixed)
    pass_values:'map'=map(str,unpacked)
    table(pass_values,aligns,widths)
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