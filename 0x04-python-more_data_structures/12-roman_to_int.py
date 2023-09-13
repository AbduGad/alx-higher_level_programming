#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    sum = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for i in roman_string:
        if roman_dict[i] > prev:
            sum += roman_dict[i] - prev * 2
        else:
            sum += roman_dict[i]
        prev = roman_dict[i]
    return sum
