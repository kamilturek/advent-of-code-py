def parse(input_data: str) -> list[int]:
    return list(map(int, input_data.splitlines()))


def solve(input_data: str) -> int:
    measurements = parse(input_data)
    windows = [sum(measurements[i : i + 3]) for i in range(len(input_data))]
    return sum(1 for prev, curr in zip(windows, windows[1:]) if curr > prev)
