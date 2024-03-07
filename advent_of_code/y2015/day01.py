from utils.read_file import get_lines

from pathlib import Path

data_file = Path.cwd() / "advent_of_code" / "y2015" / "data" / "day01.data"

def part_one() -> int:
    floor = 0

    for line in get_lines(data_file):
        for char in line:
            if char == '(':
                floor += 1
            else:
                floor -= 1

    return floor

def part_two() -> int:
    floor = 0
    position = 1

    for line in get_lines(data_file):
        for char in line:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1

            if floor <= -1:
                return position
            
            position += 1

    return 0
