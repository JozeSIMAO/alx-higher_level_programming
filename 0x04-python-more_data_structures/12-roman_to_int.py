#!/usr/bin/python3
def roman_to_int(roman_string):
    """roman to integer"""
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_value = 0

    for symbol in roman_string[::-1]:
        value = roman_num[symbol]
        if value >= prev_value:
            num += value
        else:
            num -= value
            prev_value = value
    return (num)
