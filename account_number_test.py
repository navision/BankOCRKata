import unittest
from account_number import AccountNumber


class AccountNumberTest(unittest.TestCase):
    def test_valid_account_number_passes_checksum(self):
        self.assertTrue(AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, 5]).is_valid())
        self.assertTrue(AccountNumber([4, 5, 7, 5, 0, 8, 0, 0, 0]).is_valid())

    def test_invalid_account_number_fails_checksum(self):
        self.assertFalse(AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, 6]).is_valid())
        self.assertFalse(AccountNumber([4, 5, 7, 5, 0, 8, 0, 0, 1]).is_valid())
        self.assertFalse(AccountNumber([9, 9, 9, 9, 9, 9, 9, 9, 9]).is_valid())

    def test_equality_works(self):
        self.assertNotEqual(AccountNumber([0]), "not account number")
        self.assertNotEqual("not account number", AccountNumber([0]))
        self.assertNotEqual(AccountNumber([0]), None)
        self.assertNotEqual(None, AccountNumber([0]))
        self.assertEqual(AccountNumber([0]), AccountNumber([0]))

    def test_account_number_with_all_digits_is_legible(self):
        self.assertTrue(AccountNumber([3, 4, 5, 8, 8, 2, 8, 6, 5]).is_legible())
        self.assertTrue(AccountNumber([9, 9, 9, 9, 9, 9, 9, 9, 9]).is_legible())

    def test_account_number_with_none_is_not_legible(self):
        self.assertFalse(AccountNumber([None]).is_legible())
        self.assertFalse(AccountNumber([3, 4, 5, 8, 8, 2, 8, None, 5]).is_legible())

    def test_illegible_account_number_is_also_invalid(self):
        illegible_number = AccountNumber([3, 4, 5, 8, 8, 2, 8, None, 5])
        self.assertFalse(illegible_number.is_legible())
        self.assertFalse(illegible_number.is_valid())
