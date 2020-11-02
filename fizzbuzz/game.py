import click
import sys

from .number_util import is_positive_integer
from .fizzbuzz import process


@click.command()
@click.option('-n', default=100, help='A positive integer')
def main(n):
    # Validate input
    if not is_positive_integer(n):
        print("the value of n must be a positive, non-zero integer")
        sys.exit()

    # Iterate from 1 to n inclusive and print FizzBuzz
    for i in range(1, n + 1):
        print(process(i))


if __name__ == '__main__':
    main()
