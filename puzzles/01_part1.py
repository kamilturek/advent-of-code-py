def parse(input_data: str) -> list[int]:
    return list(map(int, input_data.splitlines()))


def solve(input_data: str) -> int:
    measurements = parse(input_data)
    return sum(
        1 for prev, curr in zip(measurements, measurements[1:]) if curr > prev
    )
