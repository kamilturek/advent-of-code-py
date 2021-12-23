def fuel_burn(src: int, dest: int) -> int:
    n = abs(src - dest)
    return n * (n + 1) // 2


def parse(input_data: str) -> list[int]:
    return list(map(int, input_data.split(',')))


def solve(input_data: str) -> int:
    positions = parse(input_data)
    return min(
        sum(fuel_burn(x, y) for y in positions) for x in range(max(positions))
    )
