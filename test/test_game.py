import unittest
import game


class TestGame(unittest.TestCase):

    def test_when_playing_with_a_negative_number_then_return_an_error(self):
        results = game.play(-1)
        self.assertEqual(1, len(results))
        self.assertEqual("the value of n must be a positive, non-zero integer", results[0])

    def test_when_playing_with_zero_then_then_return_an_error(self):
        results = game.play(0)
        self.assertEqual(1, len(results))
        self.assertEqual("the value of n must be a positive, non-zero integer", results[0])

    def test_when_playing_with_a_positive_number_then_return_the_same_number_of_results(self):
        results = game.play(99)
        self.assertEqual(99, len(results))

    def test_when_playing_for_15_then_return_fizz_buzz_results(self):
        results = game.play(15)
        self.assertEqual(15, len(results))
        self.assertEqual("1", results[0])
        self.assertEqual("2", results[1])
        self.assertEqual("Fizz", results[2])
        self.assertEqual("4", results[3])
        self.assertEqual("Buzz", results[4])
        self.assertEqual("Fizz", results[5])
        self.assertEqual("7", results[6])
        self.assertEqual("8", results[7])
        self.assertEqual("Fizz", results[8])
        self.assertEqual("Buzz", results[9])
        self.assertEqual("11", results[10])
        self.assertEqual("Fizz", results[11])
        self.assertEqual("13", results[12])
        self.assertEqual("14", results[13])
        self.assertEqual("FizzBuzz", results[14])
