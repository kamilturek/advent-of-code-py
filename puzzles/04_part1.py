from dataclasses import dataclass


@dataclass
class Point:
    number: int
    marked: bool = False

    def __post_init__(self) -> None:
        self.number = int(self.number)

    def __eq__(self, other: object) -> bool:
        return self.number == other

    def __bool__(self) -> bool:
        return self.marked

    def mark(self) -> None:
        self.marked = True


class Board:
    def __init__(self, board: list[list[Point]]) -> None:
        self.board = board

    @classmethod
    def from_str(cls, raw_board: str) -> 'Board':
        return cls(
            [
                [Point(number) for number in row.split()]
                for row in raw_board.split('\n')
            ]
        )

    def mark(self, number: str) -> None:
        for row in self.board:
            for point in row:
                if point.number == number:
                    point.mark()

    def has_won(self) -> bool:
        any_row_marked = any(all(row) for row in self.board)
        any_col_marked = any(all(col) for col in zip(*self.board))
        return any_row_marked or any_col_marked

    def score(self):
        return sum(
            point.number
            for row in self.board
            for point in row
            if point.marked is False
        )


class Game:
    def __init__(self, numbers: list[set], boards: list[Board]) -> None:
        self.numbers = numbers
        self.boards = boards

    def play(self) -> tuple[Board, int]:
        for number in self.numbers:
            for board in self.boards:
                board.mark(number)
                if board.has_won():
                    return board, number


def parse(input_data: str) -> Game:
    raw_numbers, *raw_boards = input_data.split('\n\n')

    numbers = list(map(int, raw_numbers.split(',')))
    boards = [Board.from_str(raw_board) for raw_board in raw_boards]

    return Game(numbers=numbers, boards=boards)


def solve(input_data: str) -> int:
    game = parse(input_data)
    winner, last_number = game.play()
    return winner.score() * last_number
