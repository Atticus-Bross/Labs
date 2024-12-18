from math import isclose

from lab6 import *


def test_fetch() -> None:
    """test_fetch() Tests the fetch function"""
    assert fetch('abc', 0, 1) == ('a', 'b')
    assert fetch({1: 2, 3: 4, 5: 6}, 3, 5) == (4, 6)
    assert fetch([1, 2, 3, 4, 5], 0, 2, 4) == (1, 3, 5)
    assert fetch((1, 2, 3, 4, 5), 1, 3) == (2, 4)


def test_variance() -> None:
    """test_variance() Tests the variance function"""
    assert variance((1, 1, 1, 1)) == 0
    assert variance((1, 2, 3, 4, 5)) == 2
    assert variance((7, 9, 5, 3, 11)) == 8
    assert variance({'a': 7, 'b': 9, 'c': 5, 'd': 3, 'e': 11}) == 8


def test_replace() -> None:
    """test_replace() Tests the replace function"""
    test_list: list = [0, 2, 2, 0, 2, 0]
    replace(test_list, 0, 1)
    assert test_list == [1, 2, 2, 1, 2, 1]
    test_list = [True, None, False, None, True]
    replace(test_list, None, 42)
    assert test_list == [True, 42, False, 42, True]
    test_list = [0, 0, 0, (1, 2), (1, 2)]
    replace(test_list, (1, 2), 12)
    assert test_list == [0, 0, 0, 12, 12]
    test_list = [0, 0, 0]
    replace(test_list, (1, 2), 12)
    assert test_list == [0, 0, 0]


def test_query_county() -> None:
    """test_query_county() Tests the query_county function"""
    # unpack the one string in the tuple before sending it to int
    assert query_county(data[0], lambda x: int(*x), None, 'fips') == 31039
    assert query_county(data[1], lambda x: x[0] + x[1], None, 'name', 'state') == 'lancaster countyNE'
    assert query_county(data[2], lambda x: x[0] - x[1], 'noaa', 'prcp', 'snow') == 5.5
    assert (query_county(data[3], lambda x: x[0] * x[1] - x[2], 'age', '0-4', '5-9', '10-14')
            == -0.05740344015901054)


def test_temp_variance() -> None:
    """test_variance() Tests the variance function"""
    assert temp_variance(data[0]) == 365.9050000000001
    assert temp_variance(data[1]) == 348.186875
    assert temp_variance(data[2]) == 332.0118749999999


def test_growth() -> None:
    """test_growth() Tests the variance function"""
    assert growth(data[3]) == -3.8650233337322004
    assert growth(data[4]) == -1.6225634324294893
    assert growth(data[5]) == -8.453662378577054


def test_deadlyness() -> None:
    """test_deadlyness() Tests the deadlyness function"""
    assert isclose(deadlyness(data[6]), .05095238095238095)
    assert isclose(deadlyness(data[7]), .0047619047619047616)
    assert isclose(deadlyness(data[8]), .005238095238095238)


def test_education() -> None:
    """test_education() Tests the education function"""
    assert isclose(education(data[9]), .224)
    assert isclose(education(data[10]), .207)
    assert isclose(education(data[11]), .250)


def test_portion_female() -> None:
    """test_portion_female() Tests the portion_female function"""
    assert isclose(portion_female(data[12]), 51.54362416107383)
    assert isclose(portion_female(data[13]), 50.59422750424448)
    assert isclose(portion_female(data[14]), 51.05024127164348)


def test_oldness() -> None:
    """test_oldness() Tests the oldness function"""
    assert isclose(oldness(data[15]), 15.382452193475815)
    assert isclose(oldness(data[16]), 26.166568222090963)
    assert isclose(oldness(data[17]), 19.619293615587624)


def test_youngness() -> None:
    """test_youngness() Tests the youngness function"""
    assert isclose(youngness(data[18]), 26.888371648120396)
    assert isclose(youngness(data[19]), 26.092930302273293)
    assert isclose(youngness(data[20]), 26.57428791377983)


def test_age_variance() -> None:
    """test_age_variance() Tests the age_variance function"""
    assert isclose(age_variance(data[21]), 0.0001782786942683424)
    assert isclose(age_variance(data[22]), 0.00011766529826546195)
    assert isclose(age_variance(data[23]), 0.00020695619312116284)


def test_employees() -> None:
    """test_employees() Tests the age_variance function"""
    assert employees(data[24]['industry']) == (4, 206, 652, 77, 609, 42, 53, 213, 6, 101, 31, 692, 11, 325, 83)
    assert employees(data[25]['industry']) == (22, 254, 7, 265, 418, 174, 921, 379, 208, 44, 165, 27, 272, 9, 424
                                               , 118, 365, 325, 4)
    assert employees(data[26]['industry']) == (58, 42, 137, 134, 67, 50, 18, 14, 249, 58, 59)


def test_raw_employment() -> None:
    """test_raw_employment() Tests the raw_employment function"""
    assert isclose(raw_employment(fetch(data[24], 'population', 'industry')), 28.81135752064582)
    assert isclose(raw_employment(fetch(data[25], 'population', 'industry')), 16.766991770801584)
    assert isclose(raw_employment(fetch(data[26], 'population', 'industry')), 16.995971609437943)


def test_employment() -> None:
    """test_employment() Tests the employment function"""
    assert isclose(employment(data[24]), 28.81135752064582)
    assert isclose(employment(data[25]), 16.766991770801584)
    assert isclose(employment(data[26]), 16.995971609437943)


def test_capitalize() -> None:
    """test_capitalize() Tests the employment function"""
    assert capitalize('') == ''
    assert capitalize('Abc F&d #2$') == 'Abc F&d #2$'
    assert capitalize('test square Cube %f4') == 'Test Square Cube %f4'


def test_full_name() -> None:
    """test_full_name() Tests the full_name function"""
    assert full_name(data[27]) == 'Dawes County, NE'
    assert full_name(data[100]) == 'Okanogan County, WA'
    assert full_name(data[200]) == 'Davison County, SD'


def test_zip_map_sort() -> None:
    """test_zip_map_sort() Tests the zip_map_sort function"""
    assert zip_map_sort('acb', lambda x: x * 2) == [('a', 'aa'), ('b', 'bb'), ('c', 'cc')]
    assert zip_map_sort((3, 2, 1), lambda x: x ** 2) == [(1, 1), (2, 4), (3, 9)]
    assert zip_map_sort([2], lambda x: x // 2) == [(2, 1), ]


def test_criteria_winner() -> None:
    """test_criteria_winner() Tests the criteria_winner function"""
    try:
        criteria_winner([], 'max')
        assert False
    except ValueError:
        pass
    try:
        criteria_winner([(3, 3)], 'square')
        assert False
    except ValueError:
        pass
    assert criteria_winner([(data[3], 3), (data[4], 5), (data[0], 15)], 'max') == ('Cuming County, NE',)
    assert criteria_winner([(data[1], 3), (data[0], 5), (data[2], 9)], 'min') == ('Lancaster County, NE',)
    assert criteria_winner([(data[0], 3), (data[1], 3), (data[2], 3)], 'min') == (
        'Cuming County, NE', 'Lancaster County, NE', 'Nuckolls County, NE')
    assert criteria_winner([(data[0], 3), (data[1], 3), (data[2], 3)], 'max') == (
        'Nuckolls County, NE', 'Lancaster County, NE', 'Cuming County, NE')


def test_top5() -> None:
    """test_top5() Tests the top5 function"""
    try:
        top5([], 'max')
        assert False
    except ValueError:
        pass
    try:
        top5([(3, 3)], 'square')
        assert False
    except ValueError:
        pass
    assert top5([(data[0], 3), (data[1], 3), (data[2], 3)], 'min') == (
    'Cuming County, NE', 'Lancaster County, NE', 'Nuckolls County, NE')
    assert top5([(data[0], 3), (data[1], 3), (data[2], 3)], 'max') == (
    'Nuckolls County, NE', 'Lancaster County, NE', 'Cuming County, NE')
    assert top5([(data[0], 1), (data[1], 2), (data[2], 3), (data[3], 4), (data[4], 5), (data[5], 6)], 'min') == (
    'Cuming County, NE', 'Lancaster County, NE', 'Nuckolls County, NE', 'Keith County, NE', 'Phelps County, NE')
    assert top5([(data[0], 1), (data[1], 2), (data[2], 3), (data[3], 4), (data[4], 5), (data[5], 6)], 'max') == (
    'Webster County, NE', 'Phelps County, NE', 'Keith County, NE', 'Nuckolls County, NE', 'Lancaster County, NE')


def test_text_list() -> None:
    """test_text_list() Tests the text_list function"""
    try:
        assert text_list()
        assert False
    except ValueError:
        pass
    assert text_list('a') == 'a'
    assert text_list('a', 'b') == 'a and b'
    assert text_list('a', 'b', 'c') == 'a; b; and c'
    assert text_list('a', 'b', 'c', 'd') == 'a; b; c; and d'
    assert text_list('a', 'b', 'c', sep=',') == 'a, b, and c'


def test_table_row() -> None:
    """test_table_row() Tests the table_row function"""
    try:
        assert table_row()
        assert False
    except ValueError:
        pass
    assert table_row('a') == '|a|'
    assert table_row('a', 'b') == '|a|b|'
    assert table_row('a', 'b', 'c') == '|a|b|c|'


test_fetch()
test_variance()
test_replace()
test_query_county()
test_temp_variance()
test_growth()
test_deadlyness()
test_education()
test_portion_female()
test_oldness()
test_youngness()
test_age_variance()
test_employees()
test_raw_employment()
test_employment()
test_capitalize()
test_full_name()
test_zip_map_sort()
test_criteria_winner()
test_top5()
test_text_list()
test_table_row()
# test file writing functions
with open('test.md', 'w') as mdfile:
    # test header
    try:
        mdfile.write(header('a', 7))
        assert False
    except ValueError:
        pass
    try:
        mdfile.write(header('a', 0))
        assert False
    except ValueError:
        pass
    mdfile.write(header('test', 1))
    mdfile.write(header('test', 3))
    mdfile.write(header('test', 6))
    # test win_statement
    mdfile.write(win_statement([(data[0], 1), (data[1], 2), (data[2], 3), (data[3], 4), (data[4], 5), (data[5], 6)],
                               'Most Testable', 'max'))
    mdfile.write(win_statement([(data[0], 1), (data[1], 2), (data[2], 3), (data[3], 4), (data[4], 5), (data[5], 6)],
                               'Most Testable', 'min', 'has'))
    mdfile.write(win_statement([(data[0], 1), (data[1], 2), (data[2], 3), (data[3], 4), (data[4], 5), (data[5], 5)],
                               'Most Testable', 'max'))
    mdfile.write(win_statement([(data[0], 1), (data[1], 1), (data[2], 1), (data[3], 4), (data[4], 5), (data[5], 6)],
                               'Most Testable', 'min', 'has'))
    # test table
    try:
        mdfile.write(table(1))
        assert False
    except ValueError:
        pass
    try:
        mdfile.write(table(2, 'a', 'b', 'c'))
        assert False
    except ValueError:
        pass
    try:
        mdfile.write(table(2, 'a', 'b'))
        assert False
    except ValueError:
        pass
    mdfile.write(table(2, 'a', 'b', 'c', 'd'))
    mdfile.write(table(3, 'aaa', 'bjk', 'as', 'asd', 'asd', 're'))
    mdfile.write(table(2, 'a', 'b', 'c', 'd', 'e', 'f'))
    try:
        write_lines(mdfile)
        assert False
    except ValueError:
        pass
    # test win_table
    mdfile.write(win_table([(data[0], 1), (data[1], 2), (data[2], 3), (data[3], 4), (data[4], 5), (data[5], 6)], 'max',
                           'Test Table', 'noaa', 'temp-jan', 'temp-apr'))
    mdfile.write(win_table([(data[0], 1), (data[1], 2), (data[2], 3), (data[3], 4), (data[4], 5), (data[5], 6)], 'min',
                           'Test Table', None, 'fips', 'state', extra=('Test', 1, 2, 3, 4, 5)))
    # test subsection
    write_lines(mdfile, *subsection('Temperature Variation', temp_variance, 'most temperature variation',
                                    'least temperature variation', 'Temperature Variation', 'noaa', 'temp-jan',
                                    'temp-apr', 'temp-jul', 'temp-oct', end='has'))
    write_lines(mdfile, *subsection('Employment', employment, 'highest employment', 'highest unemployment',
                                    'Percentage Employed', 'population', '2019', 'total-employees', end='has'))
    # test write lines
    write_lines(mdfile, header('test', 1), header('test', 2), 'test', header('test', 3), table(2, 'a', 'b', 'c', 'd'),
                header('test', 2))
    write_lines(mdfile, 'test', header('test', 1), 'test', 'test', table(2, 'a', 'b', 'c', 'd'), 'test')
    write_lines(mdfile, table(2, 'a', 'b', 'c', 'd'), header('test', 5), table(2, 'a', 'b', 'c', 'd'), 'test',
                table(2, 'a', 'b', 'c', 'd'), table(2, 'a', 'b', 'c', 'd'))
