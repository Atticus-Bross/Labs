"""Module implementing functions for:

Creating Tables
Viewing Tables
Creating Zipper Merges
Applying a Caesar Cypher to Text

Completed by Atticus Bross on 2024-10-22"""
def create_table(header:list|dict,data:list[list,...]|list[dict,...])->list[str,...]:
    """create_table(header, data)
    Creates a list of strings describing the rows of a Markdown table

    header: a list of headers
    data: a list of the data values"""
    if len(header)<1:
        raise ValueError('there must be at least one header')
    if len(data)<1:
        raise ValueError('there must be at least one data point')
    same_len_error(data)
    data_type:type=check_data_type(data)
    #whether all the sequence in data are the same length has already been checked
    if data_type==list and len(header)!=len(data[0]):
        raise ValueError('there must be as many headers as there are columns')
    col:list=columns(header,data)
    col_types:'map'=map(type,col)
    aligns:'map'=map(alignment,col_types)
    widths:'map'=map(min_width,col)
    return table_text(col,aligns,widths)