import unittest
from fizzbuzz import fizz_buzz


class TestFizzbuzz(unittest.TestCase):

    def test_when_processing_a_number_not_divisible_by_three_or_five_then_the_original_number_should_be_returned(self):
        self.assertEqual(str(2), fizz_buzz.process(2))

    def test_when_processing_a_number_divisible_by_three_then_fizz_should_be_returned(self):
        self.assertEqual('Fizz', fizz_buzz.process(3))

    def test_when_processing_a_number_divisible_by_five_then_buzz_should_be_returned(self):
        self.assertEqual('Buzz', fizz_buzz.process(5))

    def test_when_processing_a_number_divisible_by_three_and_five_then_fizz_buzz_should_be_returned(self):
        self.assertEqual('FizzBuzz', fizz_buzz.process(15))
