"""Stack
   Simple solution for pretty-printing a dictionary, probably of local or global variables.
"""

def right_justify(content: str, width: int) -> str:
    """Returns a right justified string containing content relative to column size width"""
    if len(content) > width:
        return content
    padding = ' ' * (width - len(content))
    return padding + content


def print_frame(identifier: str, variables: dict, step=True) -> None:
    """Pretty print the states of variables with a label identifier.
    For use with `locals()` and `globals()`"""
    frame = ' ' + identifier + ' '
    pointer = ' -> '
    name_width = value_width = 0
    for key in variables.keys():
        if len(key) > name_width:
            name_width = len(key)
        if len(str(variables[key])) > value_width:
            value_width = len(str(variables[key]))
    frame_width = len(' ') + name_width + len(pointer) + value_width + len(' ')
    frame = frame + '\n+' + ('-' * frame_width) + '+\n'
    for key, value in variables.items():
        frame = frame + '| ' \
                      + right_justify(key, name_width) \
                      + pointer \
                      + str(value) \
                      + ' ' * (value_width - len(str(value))) + ' |\n'
    frame = frame + '+' + ('-' * frame_width) + '+'
    print(frame)
    if step:
        input()
