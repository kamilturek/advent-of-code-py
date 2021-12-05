import importlib
import os
import re

import click


def _get_puzzles():
    puzzles_dir = os.path.join(os.path.dirname(__file__), 'puzzles')
    puzzle_pattern = re.compile(r'^\d{2}_part\d\.py$')
    return [
        filename.replace('.py', '')
        for filename in os.listdir(puzzles_dir)
        if puzzle_pattern.match(filename)
    ]


@click.command()
@click.argument('puzzle', type=click.Choice(_get_puzzles()))
@click.argument(
    'input_path',
    type=click.Path(exists=True, dir_okay=False, resolve_path=True),
)
def run(puzzle: str, input_path: str):
    puzzle_module = importlib.import_module(f'puzzles.{puzzle}')

    with open(input_path) as f:
        input_data = f.read()

    click.echo(puzzle_module.solve(input_data))


if __name__ == '__main__':
    run()
