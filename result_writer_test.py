import StringIO
import unittest
from account_number import AccountNumber
from result_writer import ResultWriter


class ResultWriterTest(unittest.TestCase):
    def test_good_account_number_works(self):
        good_account = AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, 5])
        self.assertTrue(good_account.is_valid())
        self.assertTrue(good_account.is_legible())
        self.assertEqual("345882865\t", ResultWriter().output_for(good_account))

    def test_invalid_account_number_has_appropriate_status(self):
        invalid_account = AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, 6])
        self.assertFalse(invalid_account.is_valid())
        self.assertTrue(invalid_account.is_legible())
        self.assertEqual("345882866\tERR", ResultWriter().output_for(invalid_account))

    def test_illegible_account_number_has_appropriate_status_and_digit_masking(self):
        illegible_account = AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, None])
        self.assertFalse(illegible_account.is_legible())
        self.assertEqual("34588286?\tILL", ResultWriter().output_for(illegible_account))

    def test_outputs_multiple_account_numbers_with_proper_formatting(self):
        good_account = AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, 5])
        invalid_account = AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, 6])
        illegible_account = AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, None])
        stream = StringIO.StringIO()
        ResultWriter().write_all(stream, [good_account, invalid_account, illegible_account])
        actual = stream.getvalue()
        expected = "345882865\t\n345882866\tERR\n34588286?\tILL\n"
        self.assertEqual(expected, actual)

