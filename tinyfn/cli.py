import os
import sys

import click

from .service import evaluate


@click.command()
@click.option('--path', default='.', help='path to project or repository')
@click.option('--max-length', default=50, help='Max line count for a function')
def main(path: str, max_length: int):
    try:
        fpath = full_path(path)
    except AssertionError:
        raise click.BadParameter(
            'path specified needs to be a directory',
            param_hint=['--path']
        )

    try:
        evaluate(fpath, max_length)
    except AssertionError:
        # TODO: log
        print('ERROR')
        sys.exit(1)
    else:
        print('OK')
        sys.exit(0)


def full_path(path: str):
    if path == '.':
        return os.getcwd()
    assert os.path.isdir(path)
    if os.path.isabs(path):
        return path
    return os.path.abspath(path)


if __name__ == '__main__':
    main()
