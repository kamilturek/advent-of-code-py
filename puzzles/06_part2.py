from collections import Counter


class ShiftableCounter(Counter):
    def shift(self, min: int, max: int) -> 'ShiftableCounter':
        shifted_counter = self.__class__()
        for k, v in self.items():
            shifted_counter[k - 1 if k - 1 >= min else max] += v
        return shifted_counter


class School:
    def __init__(self, timers: list[int]) -> None:
        self.timers = ShiftableCounter(timers)
        self.sum = len(timers)

    def tick(self, days: int) -> None:
        for _ in range(days):
            income = self.timers[0]
            self.sum += income
            self.timers = self.timers.shift(0, 6)
            self.timers[8] += income


def parse(input_data: str) -> School:
    return School(list(map(int, input_data.split(','))))


def solve(input_data: str) -> int:
    school = parse(input_data)
    school.tick(256)
    return school.sum
