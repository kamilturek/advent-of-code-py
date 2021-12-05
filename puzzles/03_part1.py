from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class Report:
    records: list[str]

    @property
    def record_size(self) -> int:
        return len(self.records[0])

    def most_common_at(self, position: int) -> str:
        return Counter(
            record[position] for record in self.records
        ).most_common()


def power_consumption(report: Report) -> int:
    gamma = ''.join(
        report.most_common_at(position)[0][0]
        for position in range(report.record_size)
    )
    epsilon = ''.join(
        report.most_common_at(position)[-1][0]
        for position in range(report.record_size)
    )

    return int(gamma, 2) * int(epsilon, 2)


def parse(input_data: str) -> Report:
    return Report(input_data.splitlines())


def solve(input_data: str) -> str:
    report = parse(input_data)
    return power_consumption(report)
