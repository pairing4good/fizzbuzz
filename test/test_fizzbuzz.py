import unittest
import fizz_buzz


class TestFizzbuzz(unittest.TestCase):

    def test_one(self):
        self.assertEqual(str(1), fizz_buzz.process(1))

    def test_one(self):
        self.assertEqual(str(2), fizz_buzz.process(2))

    def test_fizz(self):
        self.assertEqual('Fizz', fizz_buzz.process(3))

    def test_buzz(self):
        self.assertEqual('Buzz', fizz_buzz.process(5))

    def test_fizzbuzz(self):
        self.assertEqual('FizzBuzz', fizz_buzz.process(15))
