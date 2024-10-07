"""Lab 3
Module implementing functions for Lab 2 exercises, as well as FizzBuzz and Ordinal Suffixes
Completed by Atticus Bross 2024-09-10 for DS-1043"""
Number = int | float
from time import time


def is_odd(number: Number) -> bool:
    """is_odd(number) This function returns true if a number is odd and false otherwise. number: the number being checked"""
    return number % 2 == 1


def is_even(number: Number) -> bool:
    """is_even(number) This function returns true if a number is even and false otherwise. number: the number being checked"""
    return number % 2 == 0


def time_elapsed(timestamp: int) -> tuple[int, int, int, int]:
    """time_elapsed(timestamp) This function takes a timestamp and returns a tuple that contains the days, hours, minutes, and seconds in that order that have passed since that timestamp. timestamp: the timestamp in seconds"""
    """determines the number of seconds that have passed between now and the timestamp and then rounds it to the
    nearest second"""
    time_passed = round(time() - timestamp)
    # there are 86400 seconds in a day, and the int function removes the fractional part
    days = int(time_passed / 86400)
    days_in_seconds = days * 86400
    """days * 86400 is the number of days expressed in seconds, so the number of seconds remaining after it is
    subtracted is the number of seconds minus the number of whole days. There are 3600 seconds in an hour"""
    hours = int((time_passed - days_in_seconds) / 3600)
    hours_in_seconds = hours * 3600
    minutes = int((time_passed - days_in_seconds - hours_in_seconds) / 60)
    minutes_in_seconds = minutes * 60
    seconds = time_passed - days_in_seconds - hours_in_seconds - minutes_in_seconds
    return days, hours, minutes, seconds


def area(length: Number, width: Number) -> Number:
    """area(length, width) This function takes the length and width of a rectangle and returns its area. length: length of the rectangle | width: width of the rectangle"""
    return length * width


def perimeter(length: Number, width: Number) -> Number:
    """perimeter(length, width) This function takes the length and width of a rectangle and returns its perimeter. length: length of the rectangle | width: width of the rectangle"""
    return length * 2 + width * 2


def volume(length: Number, width: Number, height: Number) -> Number:
    """volume(length, width, height) This function takes the length, width, and height of a rectangular prism and returns its volume. length: length of the prism width: | width of the prism | height: height of the prism"""
    return length * width * height


def surface_area(length: Number, width: Number, height: Number) -> Number:
    """volume(length, width, height) This function takes the length, width, and height of a rectangular prism and returns its volume. length: length of the prism | width: width of the prism | height: height of the prism"""
    return 2 * area(length, width) + 2 * area(length, height) + 2 * area(width, height)


def get_square_color(column: int, row: int) -> str:
    """get_square_color(column, row) This function returns the color of a square on a 7 by 7 alternating color square board with (0,0) being white and returns a blank string. column: the column of the square | row: the row of the square"""
    # checks if the coordinates are in bounds
    if 0 <= column <= 7 and 0 <= row <= 7:
        """Moving from a white to black square or vise versa requires adding or subtracting 1 from either the column or 
        the row, this changes the sum from even to odd, or from odd to even, moving back to black or white changes the
        number again, back to its original state, so for a specific color the sum of its column and row will always have
        the same even-odd state. (0,0) is white, so white square have even sums and black squares have odd sums."""
        if is_even(column + row):
            return 'white'
        else:
            return 'black'
    else:
        return ''


def prettify_time(days: int, hours: int, minutes: int, seconds: int) -> str:
    """prettify_time(days, hours, minutes, seconds) This function takes values for days, hours, minutes, and seconds and returns a string of from w days, x hours, y minutes, z seconds. If a value is zero it will be skipped. days: days in the string | hours: hours in the string | minutes: minutes in the string | seconds: seconds in the string"""
    return_string = ''
    if days != 0:
        return_string += str(days) + ' days'
        if hours != 0 or minutes != 0 or seconds != 0: return_string += ', '
    if hours != 0:
        return_string += str(hours) + ' hours'
        if minutes != 0 or seconds != 0: return_string += ', '
    if minutes != 0:
        return_string += str(minutes) + ' minutes'
        if seconds != 0: return_string += ', '
    if seconds != 0:
        return_string += str(seconds) + ' seconds'
    return return_string


def right_justify(content: str, width: int) -> str:
    """right_justify(content, width) This function returns a string that when printed will be right-justified for a given column width. content: the content of the message | width: the width of the column"""
    # the remaining width of the row after the space occupied by the content has been considered
    remaining_width = width - len(content)
    return ' ' * remaining_width + content


def center_justify(content: str, width: int) -> str:
    """center_justify(content, width) This function returns a string that when printed will be center-justified for a given column width. The text will not be perfectly centered if the width - length of content is odd. content: the content of the message | width: the width of the column"""
    # the remaining width of the row after the space occupied by the content has been considered
    remaining_width = width - len(content)
    side_widths = round(remaining_width / 2)
    return ' ' * side_widths + content


def fizz_buzz(up_to: int) -> str:
    """fizz_buzz(up_to) This function produces a string with a value for every number for 1 to up_to inclusive, if the number is divisible by neither 3 nor 5, the value is the number, if the number is just divisible by 3, the value is Fizz, if the number is just divisible by 5, the value is Buzz, if the number is divisible by 3 and 5, the value is FizzBuzz. up_to: the number to stop at"""
    return_string = ''
    for i in range(1, 1 + up_to):
        if i % 3 == 0:
            return_string += 'Fizz'
        if i % 5 == 0:
            return_string += 'Buzz'
        if i % 3 != 0 and i % 5 != 0:
            return_string += str(i)
        if i != up_to:
            return_string += ' '
    return return_string


def ordinal_suffix(number: int) -> str:
    """ordinal_suffix(number) This function takes a number and returns a string of that number with its ordinal suffix e.g. 30th, 3rd. number: the number to be given a suffix"""
    if number == 1:
        return str(number) + 'st'
    elif number == 2:
        return str(number) + 'nd'
    elif number == 3:
        return str(number) + 'rd'
    else:
        return str(number) + 'th'
