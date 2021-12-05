from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class Report:
    records: list[str]

    @property
    def record_size(self) -> int:
        return len(self.records[0])

    def count_at(self, position: int) -> Counter:
        return Counter(record[position] for record in self.records)

    def filter_at(self, position: int, value: str):
        return Report(
            [record for record in self.records if record[position] == value]
        )


def oxygen_generator_rating(report: Report) -> str:
    for position in range(report.record_size):
        counts = report.count_at(position)
        if counts['0'] == counts['1']:
            most_common = '1'
        else:
            most_common = counts.most_common()[0][0]
        report = report.filter_at(position, most_common)
        if len(report.records) == 1:
            return report.records[0]


def co2_scrubber_rating(report: Report) -> str:
    for position in range(report.record_size):
        counts = report.count_at(position)
        if counts['0'] == counts['1']:
            most_common = '0'
        else:
            most_common = counts.most_common()[-1][0]
        report = report.filter_at(position, most_common)
        if len(report.records) == 1:
            return report.records[0]


def life_support_rating(report: Report) -> int:
    oxygen = oxygen_generator_rating(report)
    co2 = co2_scrubber_rating(report)
    return int(oxygen, 2) * int(co2, 2)


def parse(input_data: str) -> Report:
    return Report(input_data.splitlines())


def solve(input_data: str) -> str:
    report = parse(input_data)
    return life_support_rating(report)
