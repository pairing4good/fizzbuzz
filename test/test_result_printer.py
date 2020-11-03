import io
import unittest
from unittest import mock
from fizzbuzz import result_printer


class TestResultPrinter(unittest.TestCase):

    def test_when_printing_a_list_of_values_then_all_of_the_results_are_printed(self):
        values = ["first", "second", "third"]
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result_printer.print_all(values)

        self.assertEqual("first\nsecond\nthird\n", fake_stdout.getvalue())
