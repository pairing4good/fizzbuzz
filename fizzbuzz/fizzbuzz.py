import click
import sys


def is_positive_integer(value):
    return value > 0


def process(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"

    if value % 3 == 0:
        return "Fizz"

    if value % 5 == 0:
        return "Buzz"

    return value.__str__()


@click.command()
@click.option('-n', default=100, help='A positive integer')
def main(n):

    # Validate input
    if not is_positive_integer(n):
        print("the value of n must be a positive, non-zero integer")
        sys.exit()

    # Iterate from 1 to n inclusive and print FizzBuzz
    for i in range(1, n+1):
        print(process(i))


if __name__ == '__main__':
    main()
