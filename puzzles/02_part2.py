from typing import Literal

Direction = Literal['forward', 'up', 'down']


def parse(input_data: str) -> list[tuple[Direction, int]]:
    return list(
        map(
            lambda command: (command[0], int(command[1])),
            [line.split() for line in input_data.splitlines()],
        )
    )


def solve(input_data: str) -> int:
    commands = parse(input_data)

    horizontal_pos = 0
    depth = 0
    aim = 0

    for direction, units in commands:
        match direction:
            case 'forward':
                horizontal_pos += units
                depth += aim * units
            case 'up':
                aim -= units
            case 'down':
                aim += units

    return horizontal_pos * depth
