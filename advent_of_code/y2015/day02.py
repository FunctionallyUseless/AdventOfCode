from utils.read_file import get_lines

from dataclasses import dataclass, field
from pathlib import Path

data_file = Path.cwd() / "advent_of_code" / "y2015" / "data" / "day02.data"

@dataclass()
class Box:
    w: int
    h: int
    l: int
    wrapping_paper_size: int = field(init=False)
    ribbon_length: int = field(init=False)

    def __post_init__(self):
        surface_area = (2 * self.l * self.w) + (2 * self.w * self.h) + (2 * self.h * self.l)
        smallest_size = min([self.l * self.w, self.w * self.h, self.h * self.l])
        self.wrapping_paper_size = surface_area + smallest_size

        bow = self.w * self.h * self.l
        a, b, _ = sorted([self.w, self.h, self.l])
        wrap = a * 2 + b * 2
        self.ribbon_length = bow + wrap


def parse_line(line: str) -> Box:
    w, h, l = line.strip().split('x')
    return Box(int(w), int(h), int(l))

def part_one() -> int:
    total = 0

    for line in get_lines(data_file):
        total += parse_line(line).wrapping_paper_size

    return total

def part_two() -> int:
    total = 0

    for line in get_lines(data_file):
        total += parse_line(line).ribbon_length

    return total