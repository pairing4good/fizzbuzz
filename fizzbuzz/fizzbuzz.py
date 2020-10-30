def is_positive_integer(value):
    return value > 0


def process(value):
    output = ''

    if value % 3 == 0:
        output += "Fizz"

    if value % 5 == 0:
        output += "Buzz"

    return value.__str__() if len(output) == 0 else output
