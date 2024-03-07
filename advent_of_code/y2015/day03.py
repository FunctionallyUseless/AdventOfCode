from utils.read_file import get_lines

from dataclasses import dataclass

from pathlib import Path

data_file = Path.cwd() / "advent_of_code" / "y2015" / "data" / "day03.data"

@dataclass(frozen=True)
class Coordinate:
    x: int = 0
    y: int = 0

def part_one() -> int:    
    coordinates = {}
    current_coordinate = Coordinate()

    for line in get_lines(data_file):
        for char in line:
            if char == '^':
                new_coordinate = Coordinate(x=current_coordinate.x, y=current_coordinate.y + 1)
                if new_coordinate in coordinates:
                    coordinates[new_coordinate] += 1
                else:
                    coordinates[new_coordinate] = 1   
                current_coordinate = new_coordinate

            elif char == 'v':
                new_coordinate = Coordinate(x=current_coordinate.x, y=current_coordinate.y - 1)
                if new_coordinate in coordinates:
                    coordinates[new_coordinate] += 1
                else:
                    coordinates[new_coordinate] = 1  
                current_coordinate = new_coordinate

            elif char == '<':
                new_coordinate = Coordinate(x=current_coordinate.x - 1, y=current_coordinate.y)
                if new_coordinate in coordinates:
                    coordinates[new_coordinate] += 1
                else:
                    coordinates[new_coordinate] = 1  
                current_coordinate = new_coordinate

            elif char == '>':
                new_coordinate = Coordinate(x=current_coordinate.x + 1, y=current_coordinate.y)
                if new_coordinate in coordinates:
                    coordinates[new_coordinate] += 1
                else:
                    coordinates[new_coordinate] = 1  
                current_coordinate = new_coordinate

    return len(coordinates)

def part_two() -> int:
    coordinates = {}

    santas_current_coordinates = Coordinate()
    robosantas_current_coordinates = Coordinate()

    sanatas_turn = True

    for line in get_lines(data_file):
        for char in line:
            if sanatas_turn:
                if char == '^':
                    santas_new_coordinate = Coordinate(x=santas_current_coordinates.x, y=santas_current_coordinates.y + 1)
                    if santas_new_coordinate in coordinates:
                        coordinates[santas_new_coordinate] += 1
                    else:
                        coordinates[santas_new_coordinate] = 1   
                    santas_current_coordinates = santas_new_coordinate

                elif char == 'v':
                    santas_new_coordinate = Coordinate(x=santas_current_coordinates.x, y=santas_current_coordinates.y - 1)
                    if santas_new_coordinate in coordinates:
                        coordinates[santas_new_coordinate] += 1
                    else:
                        coordinates[santas_new_coordinate] = 1   
                    santas_current_coordinates = santas_new_coordinate

                elif char == '<':
                    santas_new_coordinate = Coordinate(x=santas_current_coordinates.x - 1, y=santas_current_coordinates.y)
                    if santas_new_coordinate in coordinates:
                        coordinates[santas_new_coordinate] += 1
                    else:
                        coordinates[santas_new_coordinate] = 1   
                    santas_current_coordinates = santas_new_coordinate

                elif char == '>':
                    santas_new_coordinate = Coordinate(x=santas_current_coordinates.x + 1, y=santas_current_coordinates.y)
                    if santas_new_coordinate in coordinates:
                        coordinates[santas_new_coordinate] += 1
                    else:
                        coordinates[santas_new_coordinate] = 1   
                    santas_current_coordinates = santas_new_coordinate
                
            else:
                if char == '^':
                    robosantas_new_coordinate = Coordinate(x=robosantas_current_coordinates.x, y=robosantas_current_coordinates.y + 1)
                    if robosantas_new_coordinate in coordinates:
                        coordinates[robosantas_new_coordinate] += 1
                    else:
                        coordinates[robosantas_new_coordinate] = 1   
                    robosantas_current_coordinates = robosantas_new_coordinate

                elif char == 'v':
                    robosantas_new_coordinate = Coordinate(x=robosantas_current_coordinates.x, y=robosantas_current_coordinates.y - 1)
                    if robosantas_new_coordinate in coordinates:
                        coordinates[robosantas_new_coordinate] += 1
                    else:
                        coordinates[robosantas_new_coordinate] = 1   
                    robosantas_current_coordinates = robosantas_new_coordinate

                elif char == '<':
                    robosantas_new_coordinate = Coordinate(x=robosantas_current_coordinates.x - 1, y=robosantas_current_coordinates.y)
                    if robosantas_new_coordinate in coordinates:
                        coordinates[robosantas_new_coordinate] += 1
                    else:
                        coordinates[robosantas_new_coordinate] = 1   
                    robosantas_current_coordinates = robosantas_new_coordinate

                elif char == '>':
                    robosantas_new_coordinate = Coordinate(x=robosantas_current_coordinates.x + 1, y=robosantas_current_coordinates.y)
                    if robosantas_new_coordinate in coordinates:
                        coordinates[robosantas_new_coordinate] += 1
                    else:
                        coordinates[robosantas_new_coordinate] = 1   
                    robosantas_current_coordinates = robosantas_new_coordinate
            
            sanatas_turn = not sanatas_turn

    return len(coordinates)
