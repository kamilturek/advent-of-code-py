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

    route = {
        'forward': 0,
        'down': 0,
        'up': 0,
    }

    for direction, units in commands:
        route[direction] += units

    return route['forward'] * (route['down'] - route['up'])
