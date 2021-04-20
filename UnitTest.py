import unittest

from Dish import Dish
from Customer import Customer


testCase1 = Customer()
testCase2 = Dish()
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(testCase1.(), 9)
    def test_2(self):
        self.assertTrue(isinstance(testCase1.get_favorite_dishes(),str))
    def test_3(self):
        self.assertTrue(isinstance(testCase1,str))
    def test_4(self):
        self.assertIn(testCase1.avoid_dishes(), [])
    def test_5(self):
        self.assertIs(testCase1.(),'')
    def test_6(self):
        self.assertIsNotNone(testCase1.get_favorite_dishes())
    def test_7(self):
        self.assertIsNotNone(testCase1.avoid_dishes())
    def test_8(self):
        self.assertIsInstance(testCase1,Customer)
    def test_9(self):
        self.assertIsNotNone(testCase2.())
    def test_10(self):
        self.assertIs(testCase2.(),'')
    def test_11(self):
        self.assertTrue(isinstance(testCase2,str))
    def test_12(self):
        self.assertIsInstance(testCase2,Dish)
    def test_13(self):
        self.assertGreater(testCase2.(),1)


unittest.main()