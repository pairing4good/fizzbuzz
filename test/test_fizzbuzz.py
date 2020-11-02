import unittest
from fizzbuzz import fizzbuzz
from fizzbuzz import number_util


class TestFizzbuzz(unittest.TestCase):

    def test_one(self):
        self.assertEqual(str(1), fizzbuzz.process(1))

    def test_one(self):
        self.assertEqual(str(2), fizzbuzz.process(2))

    def test_fizz(self):
        self.assertEqual('Fizz', fizzbuzz.process(3))

    def test_buzz(self):
        self.assertEqual('Buzz', fizzbuzz.process(5))

    def test_fizzbuzz(self):
        self.assertEqual('FizzBuzz', fizzbuzz.process(15))


if __name__ == '__main__':
    unittest.main()
