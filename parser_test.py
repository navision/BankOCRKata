import unittest
from parser import *

FULL_ENTRY = \
    "    _  _     _  _  _  _  _ \n" + \
    "  | _| _||_||_ |_   ||_||_|\n" + \
    "  ||_  _|  | _||_|  ||_| _|\n\n"

class ParserTest(unittest.TestCase):
    def test_parses_all_digits(self):
        self.assertEqual(0, Parser().digit_from(ZERO))
        self.assertEqual(1, Parser().digit_from(ONE))
        self.assertEqual(2, Parser().digit_from(TWO))
        self.assertEqual(3, Parser().digit_from(THREE))
        self.assertEqual(4, Parser().digit_from(FOUR))
        self.assertEqual(5, Parser().digit_from(FIVE))
        self.assertEqual(6, Parser().digit_from(SIX))
        self.assertEqual(7, Parser().digit_from(SEVEN))
        self.assertEqual(8, Parser().digit_from(EIGHT))
        self.assertEqual(9, Parser().digit_from(NINE))

    def test_parses_groups_of_digits(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], Parser().digits_from((ZERO, ONE, TWO, THREE, FOUR,
                                                                               FIVE, SIX, SEVEN, EIGHT, NINE)))

    def test_non_digit_bombs(self):
        self.assertRaises(KeyError, Parser().digit_from, "JUNK")

    def test_chunking_works(self):
        self.assertEqual(["123", "456", "789"], Parser().chunk("123456789"))
        self.assertEqual(["123", "456", "78"], Parser().chunk("12345678"))

    def test_parsing_full_entry_works(self):
        self.assertEqual([[1,2,3,4,5,6,7,8,9]], Parser().parse(FULL_ENTRY.splitlines()))
        self.assertEqual([[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]], Parser().parse((FULL_ENTRY * 2).splitlines()))


if __name__ == '__main__':
    unittest.main()