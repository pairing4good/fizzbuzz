import click

import game


@click.command()
@click.option('-n', default=100, help='A positive integer')
def main(n):
    results = game.play(n)

    for result in results:
        print(result)


if __name__ == '__main__':
    main()
