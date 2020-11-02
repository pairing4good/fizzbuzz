import fizz_buzz
import number_util


def play(n):
    results = []
    if not number_util.is_positive_integer(n):
        results.append("the value of n must be a positive, non-zero integer")

    for i in range(1, n + 1):
        results.append(fizz_buzz.process(i))

    return results
