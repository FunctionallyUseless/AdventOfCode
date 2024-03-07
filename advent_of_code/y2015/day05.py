from utils.read_file import get_lines

from pathlib import Path

data_file = Path.cwd() / "advent_of_code" / "y2015" / "data" / "day05.data"

def has_three_vowels(input_string: str) -> bool:
    total_vowels = 0

    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in input_string:
        if char in vowels:
            total_vowels += 1

    return total_vowels >= 3

def has_sequential_letter(input_string: str) -> bool:
    valid_substrings = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 
                        'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr',
                        'ss','tt','uu','vv','ww','xx','yy','zz']
    
    for valid_substring in valid_substrings:
        if valid_substring in input_string:
            return True
        
    return False

def no_bad_substrings(input_string: str) -> bool:
    invalid_substrings = ['ab', 'cd', 'pq', 'xy']

    for invalid_substring in invalid_substrings:
        if invalid_substring in input_string:
            return False
    
    return True

def is_nice_string(input_string: str) -> bool:
    return has_three_vowels(input_string) and has_sequential_letter(input_string) and no_bad_substrings(input_string)

def part_one() -> int:
    total = 0

    for line in get_lines(data_file):
        if is_nice_string(line):
            total += 1

    return total
