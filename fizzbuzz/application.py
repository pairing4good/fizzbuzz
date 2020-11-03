import click
from fizzbuzz import game
from fizzbuzz import result_printer


@click.command()
@click.option('-n', default=100, help='A positive integer')
def main(n):
    results = game.play(n)
    result_printer.print_all(results)


if __name__ == '__main__':
    main()
