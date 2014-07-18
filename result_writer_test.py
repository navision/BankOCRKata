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

