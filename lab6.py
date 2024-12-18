from json import load

from lab4 import average

Number = int | float
Sequence = str | list | tuple | dict
# sequences that can contain numbers
NumList = list | tuple | dict
# indexable sequences
Indexable = str | list | tuple
with open('datasets/counties.json', 'r') as jsonfile:
    data = load(jsonfile)


def fetch(seq: Sequence, *indexes) -> tuple:
    """fetch(seq, *indexes) retrieves specific elements from a sequence

    seq: the sequence to be retrieved from
    *indexes: the indexes or keys of the items to be retrieved"""
    return_tuple: tuple = ()
    for index in indexes:
        return_tuple = return_tuple + (seq[index],)
    return return_tuple


def variance(numbers: NumList) -> Number:
    """variance(numbers) Finds the variance of a list of numbers

    numbers: the list of numbers"""
    # handle dictionaries
    if type(numbers) == dict:
        numbers = list(numbers.values())
    avg: Number = average(numbers)
    # the iterable map returns does not work well with other functions
    difs: list = list(map(lambda x: (avg - x) ** 2, numbers))
    return average(difs)


def replace(start_list: list, original, replacement) -> None:
    """replace(start_list, original, replacement) Replaces a value in a list with another value wherever it occurs

    start_list: the list the operation is to be preformed on
    original: the original value
    replacement: the value to replace the original with"""
    occurrences: int = start_list.count(original)
    # the nature of for loops handles cases where original is not in start_list automatically
    # in this case the list remains unchanged
    for i in range(occurrences):
        index: int = start_list.index(original)
        start_list.insert(index, replacement)
        start_list.remove(original)


def query_county(county: dict, f, directory, *keys):
    """query_county(county, f, directory, *keys, if_none) Gets information from a county

    county: the county to be queried
    f: the function to be preformed on the data
    directory: the key of the sub dictionary, if None then the function looks in the whole county
    *keys: the keys in the sub dictionary to be used"""
    if directory is None:
        county_data: tuple | list = fetch(county, *keys)
    else:
        county_data: tuple | list = fetch(county[directory], *keys)
    county_data = list(county_data)
    # None in this database means zero
    replace(county_data, None, 0)
    return f(county_data)


def temp_variance(county: dict) -> Number:
    """temp_variance(county) Finds the temperature variance for a county

    county: the county for which the variance is to be found"""
    return query_county(county, variance, 'noaa', 'temp-jan', 'temp-apr', 'temp-jul', 'temp-oct')


def growth(county: dict) -> Number:
    """growth(county) Finds how much a county has grown in population from the start to the end of the data

    county: the county for which the growth is to be found"""
    return query_county(county, lambda x: ((x[1] - x[0]) / x[0]) * 100, 'population', '2010', '2019')


def deadlyness(county: dict) -> Number:
    """deadlyness(county) Finds the deadlyness of a county

    county: the county for which the deadlyness is to be found"""
    return query_county(county, lambda x: sum(x) / 100, 'deaths', 'suicides', 'homicides', 'vehicle')


def education(county: dict) -> Number:
    """education(county) Finds the education of a county

    county: the county for which the education is to be found"""
    return query_county(county, lambda x: x[0] / 100, 'edu', 'bachelors+')


def portion_female(county: dict) -> Number:
    """portion_female(county) Finds the portion of a county that is female

    county: the county for which the female portion is to be found"""
    return query_county(county, lambda x: (x[1] / (x[0] + x[1])) * 100, None, 'male', 'female')


for county2 in data:
    county2['Percentage Male'] = 100 - portion_female(county2)


def oldness(county: dict) -> Number:
    """oldness(county) Finds the portion of a county that is over 65

    county: the county for which the oldness is to be found"""
    return query_county(county, lambda x: sum(x) * 100, 'age', '65-69', '70-74', '75-79', '80-84', '85+')


def youngness(county: dict) -> Number:
    """youngness(county) Finds the portion of a county that is under 20

    county: the county for which the youngness is to be found"""
    return query_county(county, lambda x: sum(x) * 100, 'age', '0-4', '5-9', '10-14', '15-19')


def age_variance(county: dict) -> Number:
    """age_variance(county) Finds the age variation for a county

    county: the county for which the age variation is to be found"""
    return query_county(county, lambda x: variance(*x), None, 'age')


def employees(industries: dict[str:dict[str:Number, ...], ...]) -> tuple[Number, ...]:
    """employees(industries) Returns a list of the employees in the given industries

    industries: the industries to be evaluated"""
    industries = list(industries.values())
    return_tuple: tuple = ()
    for industry in industries:
        return_tuple = return_tuple + (industry['employees'],)
    return return_tuple


# give information needed for later tables
for county2 in data:
    if 'industry' in county2.keys():
        county2['population']['total-employees'] = sum(employees(county2['industry']))
    else:
        county2['population']['total-employees'] = 0


def raw_employment(raw_data: tuple) -> Number:
    """raw_employment(raw_data) A function to be passed to a query_county function

    raw_data: generated by query_county, directory: None, *keys: 'population', 'industry'"""
    # raw_data[0] == population, raw_data[1] == industry
    employee_num = sum(employees(raw_data[1]))
    return (employee_num / raw_data[0]['2019']) * 100


def employment(county: dict) -> Number:
    """employment(county) Finds the employment rate for a county

    county: the county for which the employment is to be found"""
    if 'industry' in county.keys():
        return query_county(county, raw_employment, None, 'population', 'industry')
    else:
        return 0


def capitalize(string: str) -> str:
    """capitalize(string) Capitalizes the words of a string

    string: the string to be capitalized"""
    letter_equivalents: dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
                                'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P',
                                'q': 'Q', 'r': 'R', 's': 'S'
        , 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    cap_next: bool = True
    return_string: str = ''
    for character in string:
        if cap_next and character in letter_equivalents.keys():
            return_string = return_string + letter_equivalents[character]
        else:
            return_string = return_string + character
        if character == ' ':
            cap_next = True
        else:
            cap_next = False
    return return_string


def full_name(county: dict) -> str:
    """full_name(county) Gives the full name of a county

    county: the county for which the name is to be given"""
    return capitalize(county['name']) + ', ' + county['state']


def zip_map_sort(seq: Indexable, f) -> list:
    """zip_map(seq, f) Associates each value in a sequence with the value of a function of the value and sorts the result

    seq: the sequence
    f: the function"""
    f_values: 'map' = map(f, seq)
    zipped: 'zip' = zip(seq, f_values)
    return sorted(zipped, key=lambda x: x[1])


def criteria_winner(sort: list, mode: str) -> tuple[str, ...]:
    """criteria_winner(sort, mode) Finds the winning county(s) for a given criteria

    sort: sorted list of the candidates
    mode: 'max': picks the largest value 'min': picks the smallest values"""
    if len(sort) < 1:
        raise ValueError('sort must have at least one element')
    if mode == 'min':
        first = sort[0][1]
        start: int = 0
        step: int = 1
    elif mode == 'max':
        first = sort[-1][1]
        start: int = -1
        step: int = -1
    else:
        raise ValueError('mode must be either max or min')
    counties: tuple = ()
    for county, value in sort[start:None:step]:
        # the values in sort are (item, value)
        if value == first:
            counties = counties + (full_name(county),)
        else:
            break
    return counties


def top5(sort: list, mode: str) -> tuple:
    """top5(sort, mode) Gives the top 5 for a from a list

    sort: a pre-sorted list that associates each element with a value
    mode: 'max': picks the largest value 'min': picks the smallest values"""
    if len(sort) < 1:
        raise ValueError('sort must have at least one element')
    if mode == 'min':
        start: int = 0
        stop: int = 5
        step: int = 1
    elif mode == 'max':
        start: int = -1
        stop: int = -6
        step: int = -1
    else:
        raise ValueError('mode must be either max or min')
    tops: tuple = ()
    for county, value in sort[start:stop:step]:
        tops = tops + (full_name(county),)
    return tops


def text_list(*items: str, sep: str = ';') -> str:
    """text_list(*items) Gives a grammatically correct list

    *items: the items in the list
    sep: the character to separate the items with"""
    if len(items) < 1:
        raise ValueError('there must be at least one item')
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return items[0] + ' and ' + items[1]
    else:
        return_string: str = ''
        for index, item in enumerate(items):
            # not the last item
            if index != len(items) - 1:
                return_string = return_string + item + sep + ' '
            else:
                return_string = return_string + 'and ' + item
        return return_string


def table_row(*items: str) -> str:
    """table_row(*items) Generates a row of a markdown table

    *items: the items of the row"""
    if len(items) < 1:
        raise ValueError('there must be at least one item')
    row: str = '|'.join(items)
    row = '|' + row + '|'
    return row


def win_statement(sort: list, criteria: str, mode: str, end: str = 'is') -> str:
    """win_statement(sort, criteria, end='is') Creates a statement announcing the winner(s) from a sorted list

    sort: the sorted list
    criteria: the message with which to end the statement
    mode: 'max' or 'min', determines whether to choose the lowest or highest values
    end: 'x is the y' or 'x has the y'"""
    if end != 'is' and end != 'has':
        raise ValueError('end must be either is or has')
    winners: tuple = criteria_winner(sort, mode)
    if len(winners) == 1:
        return text_list(*winners) + ' ' + end + ' the ' + criteria
    else:
        # covert end to plural
        if end == 'is':
            end = 'are'
        elif end == 'has':
            end = 'have'
        return text_list(*winners) + ' ' + end + ' the ' + criteria


def header(text: str, level: int) -> str:
    """header(text, level, file) Gives header text for a markdown file

    text: the text of the header
    level: 1-6, 1 is the largest"""
    if level > 6 or level < 1:
        raise ValueError('level must be between 1 and 6')
    return '#' * level + ' ' + text


def table(col: int, *items: str) -> str:
    """table(*items) Generates a markdown table

    col: the number of columns
    *items: the items in the table"""
    if len(items) % col != 0:
        raise ValueError('the items must fit evenly into the columns')
    rows_num: int = len(items) // col
    if rows_num < 2:
        raise ValueError('there must be at least two rows')
    row1: list = list(items[0:col])
    rows: list = []
    # calculate number of rows
    for i in range(rows_num):
        # the range of indexes that correspond to rows
        rows.append(table_row(*items[col * i:col * (i + 1)]), )
    # calculate how to add the -'s
    header_indication: str = '|'
    for i in range(len(row1)):
        header_indication = header_indication + '---|'
    rows.insert(1, header_indication)
    return '\n'.join(rows)


def win_table(sort: list, mode: str, name: str, directory: str | None, *keys, extra: Indexable = ()) -> str:
    """win_table(sort, directory, *keys) Generates a table for the top 5 winners of a category

    sort: a pre-sorted list of the candidates and there associated values
    mode: 'max' or 'min', determines whether to choose the lowest or highest values
    name: the name for the associated data in sort
    directory: the directory to retrieve the additional data from, if None then the whole candidate will be searched
    *keys: the keys of the information to be retrieved
    extra: a sequence of any extra data to include starting with the name for that data"""
    if mode == 'max':
        winners: list = sort[-1:-6:-1]
    elif mode == 'min':
        winners: list = sort[0:5]
    else:
        winners: list = []
    # one for the name, extra, and comparison value
    col: int = 1 + len(keys) + 1
    if len(extra) > 0:
        col = col + 1
    rows: list = []
    if len(extra) == 0:
        rows.extend(('Name', *keys, name))
    else:
        rows.extend(('Name', *keys, extra[0], name))
    for index, winner in enumerate(winners):
        rows.append(full_name(winner[0]))
        if directory is None:
            for key in keys:
                rows.append(str(winner[0][key]))
        else:
            for key in keys:
                rows.append(str(winner[0][directory][key]))
        if len(extra) > 0:
            rows.append(str(extra[index + 1]))
        rows.append(str(winner[1]))
    return table(col, *rows)


def subsection(title: str, f, criteria1: str, criteria2, title2: str, directory: str | None, *keys
               , end: str = 'is') -> tuple[str, ...]:
    """subsection(title, f, criteria1, criteria2, title2, directory, *keys, end='is') Generates the markdown lines for a complete subsection of the report

    title: the title of the subsection
    f: the function to sort on
    criteria 1-2: the phrases to end the winner statement with
    titles 2: the title of the data used for the ranking of each candidate
    directory: the directory to retrieve the additional data from, if None then the whole candidate will be searched
    *keys: the keys of the information to be retrieved
    end: 'is' or 'has', 'x is the y' or 'x has the y'"""
    title3: str = capitalize(criteria1)
    title4: str = capitalize(criteria2)
    sort: list = zip_map_sort(data, f)
    return (header(title, 2), header(title3, 3), win_statement(sort, criteria1, 'max', end)
            , win_table(sort, 'max', title2, directory, *keys), header(title4, 3)
            , win_statement(sort, criteria2, 'min', end)
            , win_table(sort, 'min', title2, directory, *keys))


def write_lines(file, *lines: str) -> None:
    """write_lines(file, *lines) Writes lines to a markdown file, handling good practices automatically

    file: the markdown file
    *lines: the lines to be written"""
    if len(lines) < 1:
        raise ValueError('there must be at least one line to write')
    to_write: str = ''
    last_line: str = ''
    for line in lines:
        # check for headers
        if line[0] == '#':
            if last_line == 'plain':
                to_write = to_write + '\n' * 2 + line + '\n' * 2
            elif last_line == 'header' or last_line == 'table':
                to_write = to_write + line + '\n' * 2
            elif last_line == '':
                to_write = to_write + '\n' + line + '\n' * 2
            last_line = 'header'
        # check for normal text
        elif line[0] == '|':
            if last_line == 'header' or last_line == '' or last_line == 'table':
                to_write = to_write + line + '\n' * 2
            elif last_line == 'plain':
                to_write = to_write + '\n' * 2 + line + '\n' * 2
            last_line = 'table'
        else:
            if last_line == 'header' or last_line == '' or last_line == 'table':
                to_write = to_write + line
            elif last_line == 'plain':
                to_write = to_write + '<br>' + line
            last_line = 'plain'
    file.write(to_write)


# generate the report
if __name__ == '__main__':
    with open('report.md', 'w') as mdfile:
        write_lines(mdfile, header('Lab 6: Data Scavenger Hunt for Data Science', 1),
                    *subsection('Temperature Stability', temp_variance, 'most temperature stable',
                                'least temperature stable', 'Temperature Variation', 'noaa',
                                'temp-jan', 'temp-apr', 'temp-jul', 'temp-oct'),
                    *subsection('Growth', growth, 'fastest growing', 'fastest declining', 'Percentage Growth',
                                'population', '2010', '2019'),
                    *subsection('Deadliness', deadlyness, 'deadliest', 'least deadly', 'Deaths per Capita', 'deaths',
                                'suicides', 'homicides', 'vehicle'),
                    *subsection('Education', education, 'most educated', 'least educated',
                                'College Graduates per Capita', 'edu', 'bachelors+'),
                    *subsection('Gender Skewed Counties', portion_female, 'most skewed female', 'most skewed male',
                                'Percentage Female', None, 'male', 'female', 'Percentage Male'), header('Age', 2),
                    header('Oldest', 3), win_statement(zip_map_sort(data, oldness), 'oldest', 'max'),
                    win_table(zip_map_sort(data, oldness), 'max', 'Percentage over 65', 'age', '65-69', '70-74',
                              '75-79', '80-84', '85+'), header('Youngest', 3),
                    win_statement(zip_map_sort(data, youngness), 'youngest', 'max'),
                    win_table(zip_map_sort(data, youngness), 'max', 'Percentage under 20', 'age', '0-4', '5-9', '10-14',
                              '15-19'), header('Most Age Diverse', 3),
                    win_statement(zip_map_sort(data, age_variance), 'age diverse', 'min'),
                    win_table(zip_map_sort(data, age_variance), 'min', 'Age Variance', 'age', '0-4', '5-9', '10-14',
                              '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64',
                              '65-69', '70-74', '75-79', '80-84', '85+'),
                    *subsection('Employment', employment, 'highest employment', 'highest unemployment',
                                'Percentage Employed', 'population', '2019', 'total-employees', end='has'),
                    'Employment may be higher than 100% due to the activities of non-residents.')
