import unittest
import number_util


class TestInput(unittest.TestCase):

    def test_valid_input(self):
        self.assertTrue(number_util.is_positive_integer(1))
        self.assertFalse(number_util.is_positive_integer(0))
        self.assertFalse(number_util.is_positive_integer(-1))


if __name__ == '__main__':
    unittest.main()
