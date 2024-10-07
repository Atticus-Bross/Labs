"""Module implementing functions for Odd and Even, Time Elapsed, Area, Perimeter, Volume, Surface Area, Square Color,
Prettifying Time, and Right and Center Justifying
Completed by Atticus Bross 2024-09-03 for DS-1043"""
Number = int | float
from time import time
def is_odd(number: Number) -> bool:
    """This function returns true if a number is odd and false otherwise."""
    #if a number is equivalent to its integer parts then it contains no fractional parts
    if number == int(number) and number % 2 != 0: return True
    else: return False
def is_even(number: Number) -> bool:
    """This function returns true if a number is even and false otherwise."""
    # if a number is equivalent to its integer parts then it contains no fractional parts
    if number == int(number) and number % 2 == 0: return True
    else: return False
def time_elapsed(timestamp: int) -> tuple[int, int, int, int]:
    """This function takes a timestamp and returns a tuple that contains the days, hours, minutes, and seconds in that order
    that have passed since that timestamp."""
    """determines the number of seconds that have passed between now and the timestamp and then rounds it to the
    nearest second"""
    time_passed = round(time() - timestamp)
    #there are 86400 seconds in a day, and the int function removes the fractional part
    days = int(time_passed / 86400)
    """days * 86400 is the number of days expressed in seconds, so the number of seconds remaining after it is
    subtracted is the number of seconds minus the number of whole days. There are 3600 seconds in an hour"""
    hours = int((time_passed - days * 86400) / 3600)
    minutes = int((time_passed - days * 86400 - hours * 3600) / 60)
    seconds = time_passed - days * 86400 - hours * 3600 - minutes * 60
    return days, hours, minutes, seconds
def area(length: Number, width: Number) -> Number:
    """This function takes the length and width of a rectangle and returns its area."""
    return length * width
def perimeter(length: Number, width: Number) -> Number:
    """This function takes the length and width of a rectangle and returns its perimeter."""
    return length * 2 + width * 2
def volume(length: Number, width: Number, height: Number) -> Number:
    """This function takes the length, width, and height of a rectangular prism and returns its volume."""
    return length * width * height
def surface_area(length: Number, width: Number, height: Number) -> Number:
    """This function takes the length, width, and height of a rectangular prism and returns its surface area."""
    return 2 * area(length, width) + 2 * area(length, height) + 2 * area(width, height)
def get_square_color(column: int, row: int) -> str:
    """This function returns the color of a square on a 7 by 7 alternating color square board with (0,0) being white and
    returns a blank string. The function should not be used with non-integer inputs."""
    #checks if the coordinates are in bounds
    if 0 <= column <= 7 and 0 <= row <= 7:
        """Moving from a white to black square or vise versa requires adding or subtracting 1 from either the column or 
        the row, this changes the sum from even to odd, or from odd to even, moving back to black or white changes the
        number again, back to its original state, so for a specific color the sum of its column and row will always have
        the same even-odd state. (0,0) is white, so white square have even sums and black squares have odd sums."""
        if is_even(column + row): return 'white'
        else: return 'black'
    else: return ''
def prettify_time(days: int, hours: int, minutes: int, seconds: int) -> str:
    """This function takes values for days, hours, minutes, and seconds and returns a string of from w days, x hours,
    y minutes, z seconds. If a value is zero it will be skipped."""
    return_string = ''
    if days != 0: return_string += str(days) + ' days'
    if hours != 0: return_string += ', ' + str(hours) + ' hours'
    if minutes != 0: return_string += ', ' + str(minutes) + ' minutes'
    if seconds != 0: return_string += ', ' + str(seconds) + ' seconds'
    return return_string
def right_justify(content: str, width: int) -> str:
    """This function returns a string that when printed will be right-justified for a given column width."""
    #the remaining width of the row after the space occupied by the content has been considered
    remaining_width = width - len(content)
    return ' ' * remaining_width + content
def center_justify(content: str, width: int) -> str:
    """This function returns a string that when printed will be center-justified for a given column width. The text will not be
    perfectly centered if the width - length of content is odd."""
    # the remaining width of the row after the space occupied by the content has been considered
    remaining_width = width - len(content)
    side_widths = round(remaining_width / 2)
    return ' ' * round(remaining_width / 2) + content