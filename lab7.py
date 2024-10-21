"""Lab 7
Module implementing functions for:

Creating Tables
Viewing Tables
Creating Zipper Merges
Applying a Caesar Cypher to Text

Completed by Atticus Bross on 2024-10-22 for DS-1043"""


from random import choice
from shutil import get_terminal_size
from string import ascii_lowercase, ascii_uppercase
from types import NoneType, UnionType
from typing import Sequence, Any, IO


def same_len_error(seq: list[list] | list[dict], error_txt: str) -> None:
    """same_len_error(seq, error_txt)
    Raises a ValueError if the sequences within seq are not all the same length

    seq: the sequence of sequences
    error_txt: the text to display for the error"""
    lengths: list = list(map(len, seq))
    if lengths.count(lengths[0]) != len(lengths):
        raise ValueError(error_txt)


def fix(value) -> str:
    """fix(value)
    Fixes a value to appear properly in a table

    value: the value"""
    if isinstance(value, NoneType):
        return ''
    elif isinstance(value, str | bool):
        return f'{value}'
    elif isinstance(value, int) and len(str(value)) > 7:
        return f'{float(value):e}'
    elif isinstance(value, float):
        rounded: str = f'{value:.2f}'
        if len(rounded) > 7:
            return f'{value:e}'
        else:
            return rounded
    else:
        return f'{value}'


def columns(values: list, cols: int) -> list[list]:
    """columns(values, cols)
    Breaks data into a given number of columns

    values: the values to be broken up
    cols: the number of columns"""
    col_len: int = len(values) // cols
    columns2: list = []
    for i in range(cols):
        col: list = []
        for j in range(col_len):
            col.append(values[i + j * cols])
        columns2.append(col)
    return columns2


def alignment(value) -> str:
    """alignment(value)
    Determines the alignment a value should have in a table

    value: the value to align"""
    if isinstance(value, int | float) and not isinstance(value, bool):
        return 'right'
    elif isinstance(value, str | bool):
        return 'left'
    else:
        raise ValueError('value must be either int, float, bool, or str')


def none_str(value) -> str:
    """non_str(value)
    Converts the value to a string, None converts to a blank string

    value: the value to convert"""
    if value is None:
        return ''
    else:
        return str(value)


def add_alignment(values: list[str], aligns: list[str]) -> list[str]:
    """add_alignment(values, aligns)
    Adds proper markdown alignment to a list of strings
    
    values: the strings to be given alignment
    aligns: should be made up of the strings 'left' and 'right'"""
    aligned: list = []
    for index, value in enumerate(values):
        if aligns[index] == 'left':
            aligned.append(f':{value}')
        elif aligns[index] == 'right':
            aligned.append(f'{value}:')
        else:
            raise ValueError("aligns must be either 'left' or 'right'")
    return aligned


def max_width(seqs: Sequence[Sequence]) -> int:
    """max_width(seqs)
    Finds the largest sequence within a sequence

    seqs: the sequence of sequences"""
    lengths: 'map' = map(len, seqs)
    return max(lengths)


def rows(values: list, rows2: int) -> list[list]:
    """rows(values, rows2)
    Breaks data up into a given number of rows

    values: the data
    rows2: the number of rows"""
    row_len: int = len(values) // rows2
    return_rows: list = []
    for i in range(rows2):
        return_rows.append(values[i * row_len:(i + 1) * row_len])
    return return_rows


def table_row(values: list[str], widths: list[int], aligns: list[str]) -> str:
    """table_row(values, widths, aligns)
    Creates the string for a row in a Markdown table

    values: the values in the row
    widths: the width each column is to be in the final table
    aligns: the alignment of each element in the row"""
    elements: list = []
    for index, value in enumerate(values):
        if aligns[index] == 'left':
            elements.append(f'{value:<{widths[index]}}')
        elif aligns[index] == 'right':
            elements.append(f'{value:>{widths[index]}}')
        else:
            raise ValueError("aligns must be either 'left' or 'right'")
    return f'|{'|'.join(elements)}|\n'


def table(values: list[str], aligns: list[str], cols: int) -> list[str]:
    """table(values, aligns, cols)
    Creates a table from a list of values and alignments

    values: a list of the values
    aligns: the alignments for each column
    cols: the number of columns"""
    cols2: list = columns(values, cols)
    # the width must be at least 4 to accommodate the minimum column specification, '---:'
    widths: list = list(map(lambda x: max(max_width(x), 4), cols2))
    rows2: list = rows(values, len(values) // cols)
    return_rows: list = []
    for index, row2 in enumerate(rows2):
        # cols is also the length of each row
        return_rows.append(table_row(row2, widths, aligns))
    # add header formatting row
    header_row: list = []
    for width in widths:
        header_row.append('-' * (width - 1))
    # add the proper semicolons to the header row
    header_row: list = add_alignment(header_row, aligns)
    return_rows.insert(1, table_row(header_row, widths, ['left', 'left', 'left', 'left']))
    return return_rows


def list_type(seq: list):
    """list_type(seq)
    Returns the second value in a list that is not None

    seq: the list"""
    for element in seq[1:]:
        if not isinstance(element, NoneType):
            return element


def deep_unpack(seq: Sequence[Sequence], ignores: type | UnionType = str) -> list:
    """deep_unpack(seq, ignores=str)
    Unpacks a sequence of sequences into a single sequence

    seq: the sequence
    ignores: the types of sequences to ignore"""
    unpacked: list = []
    for element in seq:
        if isinstance(element, Sequence) and not isinstance(element, ignores):
            # this is to avoid the infinite recursion that occurs because a string contains a string which contains a string, etc.
            if isinstance(element, str) and len(element) == 1:
                unpacked.append(element)
            else:
                unpacked.extend(deep_unpack(element, ignores))
        else:
            unpacked.append(element)
    return unpacked


def align(cols: list[list]) -> list[str]:
    """align(cols)
    Determines the alignment for a list of columns

    cols: the columns (also lists)"""
    aligns: list = list(map(list_type, cols))
    aligns = list(map(alignment, aligns))
    return aligns


def table_data(data: list, col: int) -> tuple[list[str], list[str], int]:
    """table_data(data, col)
    Creates the data to pass to the table function

    data: the data extracted from some sequence
    col: the number of columns"""
    unpacked: list = data.copy()
    unpacked = list(map(fix, unpacked))
    cols: list = columns(data, col)
    aligns: list = align(cols)
    return unpacked, aligns, col


def table_from_list(header: list, data: list[list]) -> list[str]:
    """table_from_list(header, data)
    Creates a table from a header and data that are lists of values

    header: the headers
    data: the values of the table"""
    same_len_error(data, 'all rows must be the same length')
    if len(header) != len(data[0]):
        raise ValueError('there must be as many headers as there are columns')
    unpacked: list = [*header, *deep_unpack(data)]
    return table(*table_data(unpacked, len(header)))


def table_from_dict(header: list | dict[Any:str], data: list[dict]) -> list[str]:
    """table_from_dict(header, data)
    Generates a Markdown table from a list of dictionaries

    header: either a list of keys for data or a dictionary that shares keys with data
    data: the list of dictionaries"""
    if isinstance(header, list):
        unpacked: list = header.copy()
    elif isinstance(header, dict):
        unpacked: list = list(header.values())
    else:
        raise ValueError('header must be a list or dictionary')
    for row in data:
        for key in header:
            unpacked.append(row.setdefault(key))
    return table(*table_data(unpacked, len(header)))


def create_table(header: list | dict, data: list[list | dict]) -> list[str]:
    """create_table(header, data)
    Creates a list of strings describing the rows of a Markdown table

    header: a list of headers
    data: a list of the data values"""
    data_type: type = type(data[0])
    if data_type == list:
        return table_from_list(header, data)
    elif data_type == dict:
        return table_from_dict(header, data)


def prepare_row(row: str) -> list[str]:
    """prepare_row(row)
    Prepares a row to have some of its columns removed

    row: the row"""
    values: list = row.split('|')
    values.remove('\n')
    values.remove('')
    values = list(map(lambda x: f'|{x}', values))
    return values


def remove_cols(row: str, col: int) -> str:
    """remove_cols(row, col)
    Removes a specified number of columns from a Markdown table row

    row: the row, represented as a string
    col: the number of columns to remove"""
    values: list = prepare_row(row)
    for _ in range(col):
        values.pop()
    return f'{''.join(values)}...'


def view_table(header: list | dict, data: list[list | dict], max_width: int = get_terminal_size().columns,
               file: IO | None = None) -> None:
    """view_table(header, data, max_width=os.get_terminal_size(), file=None)
    Pretty prints a table to a stream

    header: the headers of the table
    data: the data in the table
    max_width: the maximum width of the table, default is the width of the terminal
    file: the stream to print to"""
    print_table: list = create_table(header, data)
    # create_table ensures all rows are the same length
    if len(print_table[0]) > max_width:
        current_width: int = len(print_table[0])
        values: list = prepare_row(print_table[0])
        removed: int = 0
        # current_width represents the length of a string of the form '|value|value' the plus three accounts for the needed '...'
        while current_width + 3 > max_width:
            values.pop()
            removed = removed + 1
            current_width = len(''.join(values))
        rows2: list = [f'{''.join(values)}...', ]
        for row in print_table[1:]:
            rows2.append(remove_cols(row, removed))
        print(*rows2, sep='\n', file=file)
    else:
        print(*print_table, sep='', file=file, end='')


def ins_sort(list2: list) -> list:
    """ins_sort(list2)
    Sorts a list by insertion sort

    list2: the list to be sorted"""
    before: list = []
    same: list = []
    after: list = []
    insert_key = choice(list2)
    if isinstance(insert_key, str):
        insert_key = insert_key.upper()
    for value in list2:
        if isinstance(value, str):
            compare: str = value.upper()
        else:
            compare = value
        if compare < insert_key:
            before.append(value)
        elif compare > insert_key:
            after.append(value)
        else:
            same.append(value)
    if len(before) > 1:
        before = ins_sort(before)
    if len(after) > 1:
        after = ins_sort(after)
    return [*before, *same, *after]


def merge_sorted_lists(*lists: list) -> list:
    """merge_sorted_lists(*lists)
    Merges presorted lists

    *lists: the lists to be merged"""
    merged: list = []
    for list2 in lists:
        merged.extend(list2)
    merged = ins_sort(merged)
    return merged


def caesar(plaintext: str, rotation: int = 13) -> str:
    """caesar(plaintext, rotation=13)
    Applies a caesar cypher to text

    plaintext: the text to be cyphered
    rotation: how much to rotate the alphabet by"""
    cipher: dict = {}
    # modulo allows the operation to loop back around to the start of the list
    for index, letter in enumerate(ascii_lowercase):
        cipher[letter] = ascii_lowercase[(index + rotation) % len(ascii_lowercase)]
    for index, letter in enumerate(ascii_uppercase):
        cipher[letter] = ascii_uppercase[(index + rotation) % len(ascii_uppercase)]
    ciphered: str = ''
    for character in plaintext:
        if character in cipher.keys():
            ciphered = ciphered + cipher[character]
        else:
            ciphered = ciphered + character
    return ciphered
