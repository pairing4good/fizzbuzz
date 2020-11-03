import unittest
from fizzbuzz import number_util


class TestInput(unittest.TestCase):

    def test_when_evaluating_a_positive_number_then_return_true(self):
        self.assertTrue(number_util.is_positive_integer(1))

    def test_when_evaluating_zero_then_return_false(self):
        self.assertFalse(number_util.is_positive_integer(0))

    def test_when_evaluating_a_negative_number_then_return_false(self):
        self.assertFalse(number_util.is_positive_integer(-1))
