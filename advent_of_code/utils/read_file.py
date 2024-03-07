from pathlib import Path
from typing import List


def get_lines(file_path: Path) -> List[str]:
    lines = []

    with open(file_path) as file:
        for line in file:
            lines.append(line)

    return lines
