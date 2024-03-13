import unittest
import Debtors


class DebtorsTest(unittest.TestCase):

    def test_values(self):
        self.assertEqual("Число четный положительных чисел:4", Debtors.debtors([-1, -2, 3, 4, 5, 6, 7, 8, 9, 10]))
   