from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Literal


def movement(src: int, dest: int) -> Literal[-1, 0, 1]:
    if (delta := dest - src) > 0:
        return 1
    elif delta < 0:
        return -1
    return 0


@dataclass
class Point:
    x: int
    y: int

    def move_towards(self, other: 'Point') -> 'Point':
        return Point(
            self.x + movement(self.x, other.x),
            self.y + movement(self.y, other.y),
        )


@dataclass
class Line:
    start: Point
    end: Point


def parse_coords(coords: str) -> Point:
    return Point(*map(int, coords.split(',')))


def parse_line(line: str) -> Line:
    coords1, coords2 = line.split(' -> ')
    start, end = parse_coords(coords1), parse_coords(coords2)
    return Line(start, end)


def parse(input_data: str) -> list[Line]:
    raw_lines = input_data.splitlines()
    return [parse_line(line) for line in raw_lines]


def solve(input_data: str) -> int:
    lines = parse(input_data)
    board = defaultdict(Counter)

    for line in lines:
        current = line.start
        board[current.x][current.y] += 1

        while current != line.end:
            current = current.move_towards(line.end)
            board[current.x][current.y] += 1

    return sum(
        occurances >= 2
        for cols in board.values()
        for occurances in cols.values()
    )
