"""Lab 7
Module implementing functions for:

Creating Tables
Viewing Tables
Creating Zipper Merges
Applying a Caesar Cypher to Text

Completed by Atticus Bross on 2024-10-22 for DS-1043"""
def same_len_error(seq:list[list,...]|list[dict,...],error_txt:str)->None:
    """same_len_error(seq, error_txt)
    Raises a ValueError if the sequences within seq are not all the same length

    seq: the sequence of sequences
    error_txt: the text to display for the error"""
    lengths:list=list(map(len,seq))
    if lengths.count(lengths[0])!=len(lengths):
        raise ValueError(error_txt)
def create_table(header:list|dict,data:list[list,...]|list[dict,...])->list[str,...]:
    """create_table(header, data)
    Creates a list of strings describing the rows of a Markdown table

    header: a list of headers
    data: a list of the data values"""
    if len(header)<1:
        raise ValueError('there must be at least one header')
    if len(data)<1:
        raise ValueError('there must be at least one data point')
    same_len_error(data,'all rows must be the same length')
    data_type:type=check_data_type(data)
    #whether all the sequence in data are the same length has already been checked
    if data_type==list and len(header)!=len(data[0]):
        raise ValueError('there must be as many headers as there are columns')
    col:list=columns(header,data)
    col_types:'map'=map(type,col)
    aligns:'map'=map(alignment,col_types)
    widths:'map'=map(min_width,col)
    return table_text(col,aligns,widths)