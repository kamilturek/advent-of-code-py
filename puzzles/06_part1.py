from dataclasses import dataclass


@dataclass
class Lanternfish:
    timer: int

    def tick(self) -> None:
        if self.should_reproduce:
            self.timer = 6
        else:
            self.timer -= 1

    @property
    def should_reproduce(self) -> bool:
        return self.timer == 0


@dataclass
class School:
    fishes: list[Lanternfish]

    def tick(self, count: int) -> None:
        for _ in range(count):
            for fish in list(self.fishes):
                if fish.should_reproduce:
                    self.fishes.append(Lanternfish(8))
                fish.tick()


def parse(input_data: str) -> School:
    return School([Lanternfish(int(timer)) for timer in input_data.split(',')])


def solve(input_data: str) -> int:
    school = parse(input_data)
    school.tick(80)
    return len(school.fishes)
