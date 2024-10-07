""" Test of Lab 3
Module testing the Lab 3 functions
Completed by Atticus Bross 2024-09-10 for DS-1043"""

from lab3 import *

Number = int | float


def test_is_odd() -> None:
    """test_is_odd() This function tests the is_odd function."""
    assert is_odd(5)
    assert is_odd(4) is False
    assert is_odd(5.3) is False


def test_is_even() -> None:
    """test_is_even() This function tests the is_even function."""
    assert is_even(6)
    assert is_even(5) is False
    assert is_even(6.4) is False


def correct_days(timestamp: Number) -> int:
    """correct_days(timestamp) This function returns the value for days that the time_elapsed function should give. timestamp: the value used as input for the time_elapsed function being checked"""
    time_passed = round(time() - timestamp)
    # there are 86400 seconds in a day
    return int(time_passed / 86400)


def correct_hours(timestamp: Number) -> int:
    """correct_hours(timestamp) This function returns the value for hours that the time_elapsed function should give. timestamp: the value used as input for the time_elapsed function being checked"""
    time_passed = round(time() - timestamp)
    # there are 86400 seconds in a day
    days_in_seconds = int(time_passed / 86400) * 86400
    # there are 3600 seconds in an hour
    return int((time_passed - days_in_seconds) / 3600)


def correct_minutes(timestamp: Number) -> int:
    """correct_minutes(timestamp) This function returns the value for minutes that the time_elapsed function should give. timestamp: the value used as input for the time_elapsed function being checked"""
    time_passed = round(time() - timestamp)
    # there are 86400 seconds in a day
    days_in_seconds = int(time_passed / 86400) * 86400
    # there are 3600 seconds in an hour
    hours_in_seconds = int((time_passed - days_in_seconds) / 3600) * 3600
    return int((time_passed - days_in_seconds - hours_in_seconds) / 60)


def correct_seconds(timestamp: Number) -> int:
    """correct_seconds(timestamp) This function returns the value for seconds that the time_elapsed function should give. timestamp: the value used as input for the time_elapsed function being checked"""
    time_passed = round(time() - timestamp)
    # there are 86400 seconds in a day
    days_in_seconds = int(time_passed / 86400) * 86400
    # there are 3600 seconds in an hour
    hours_in_seconds = int((time_passed - days_in_seconds) / 3600) * 3600
    minutes_in_seconds = int((time_passed - days_in_seconds - hours_in_seconds) / 60) * 60
    return time_passed - days_in_seconds - hours_in_seconds - minutes_in_seconds


def test_time_elapsed() -> None:
    """test_time_elapsed() This function tests the time_elapsed function."""
    assert time_elapsed(3) == (correct_days(3), correct_hours(3), correct_minutes(3), correct_seconds(3))
    assert time_elapsed(10) == (correct_days(10), correct_hours(10), correct_minutes(10), correct_seconds(10))
    assert time_elapsed(100000) == (
    correct_days(100000), correct_hours(100000), correct_minutes(100000), correct_seconds(100000))


def test_area() -> None:
    """test_area() This function tests the area function."""
    assert area(5, 10) == 50
    assert area(4000, 5000) == 20000000
    assert area(8.7, 2.5) == 21.75


def test_perimeter() -> None:
    """test_perimeter() This function tests the perimeter function."""
    assert perimeter(5, 10) == 30
    assert perimeter(4000, 5000) == 18000
    assert perimeter(8.7, 2.5) == 22.4


def test_volume() -> None:
    """test_volume() This function tests the volume function."""
    assert volume(5, 10, 7) == 350
    assert volume(4000, 5000, 3000) == 60000000000
    assert volume(8.7, 2.5, 4.6) == 100.05


def test_surface_area() -> None:
    """test_surface_area() This function tests the surface_area function."""
    assert surface_area(5, 10, 7) == 310
    assert surface_area(4000, 5000, 3000) == 94000000
    assert surface_area(8.7, 2.5, 4.6) == 146.54


def test_get_square_color() -> None:
    """test_get_square_color() This function tests the get_square_color function."""
    assert get_square_color(0, 0) == 'white'
    assert get_square_color(3, 5) == 'white'
    assert get_square_color(5, 2) == 'black'
    assert get_square_color(-1, 5) == ''


def test_prettify_time() -> None:
    """test_prettify_time() This function tests the prettify_time function."""
    assert prettify_time(10, 10, 10, 10) == '10 days, 10 hours, 10 minutes, 10 seconds'
    assert prettify_time(0, 10, 10, 10) == '10 hours, 10 minutes, 10 seconds'
    assert prettify_time(10, 10, 10, 0) == '10 days, 10 hours, 10 minutes'
    assert prettify_time(0, 0, 0, 0) == ''


def test_right_justify() -> None:
    """test_right_justify() This function tests the right_justify function."""
    assert right_justify('hello world', 50) == 39 * ' ' + 'hello world'
    assert right_justify('hello world', 11) == 'hello world'
    assert right_justify('', 50) == 50 * ' '


def test_center_justify() -> None:
    """test_center_justify() This function tests the center_justify function."""
    assert center_justify('hello world', 50) == 20 * ' ' + 'hello world'
    assert center_justify('hello world', 11) == 'hello world'
    assert center_justify('', 50) == 25 * ' '


def test_fizz_buzz() -> None:
    """test_fizz_buzz() This function tests the fizz_buzz function."""
    assert fizz_buzz(1) == '1'
    assert fizz_buzz(15) == '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'
    assert fizz_buzz(7) == '1 2 Fizz 4 Buzz Fizz 7'


def test_ordinal_suffix() -> None:
    """test_ordinal_suffix() This function tests the ordinal_suffix function."""
    assert ordinal_suffix(1) == '1st'
    assert ordinal_suffix(2) == '2nd'
    assert ordinal_suffix(3) == '3rd'
    assert ordinal_suffix(57) == '57th'


test_is_odd()
test_is_even()
test_time_elapsed()
test_area()
test_perimeter()
test_volume()
test_surface_area()
test_get_square_color()
test_prettify_time()
test_right_justify()
test_center_justify()
test_fizz_buzz()
test_ordinal_suffix()
