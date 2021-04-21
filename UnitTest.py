import unittest

from Dish import Dish
from Customer import Customer
from db_system import db_system


testCase1 = Customer({ "_id": 1,
                      "customer_id": "1",
                      "first_name": "John",
                      "last_name": "Abraham",
                      "gender": "Male",
                      "address": "Highway 37",
                      "email": "john@gmail.com",
                      "phone": "416-1234751",
                      "favorite_dishes": ["2"],
                      "registration_date": "12-07-2020",
                      "allergy_ingredient": ["Peanut"],
                    })
testCase2 = Dish({ "_id": 2,
                  "dish_id": "2",
                  "name": "Chicken curry",
                  "rating": 5,
                  "type": "Main Dish",
                  "ingredients": "Tender Chicken",
                  "description": "onion- and tomato-based sauce, flavoured with ginger, garlic, tomato puree, chilli peppers and a variety of spices, often including turmeric, cumin, coriander, cinnamon, and cardamom",
                  "preparation_time": 40,
                  "available_date_start": "01-01-2020",
                  "available_date_end": "31-12-2020",
                  "modify_date": "01-01-2020",
                })
testCase3 = db_system()
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(testCase1.get_favorite_dishes(), ['Chicken curry'])
    def test_2(self):
        self.assertEqual(testCase1.avoid_dishes(), [])
    def test_3(self):
        self.assertFalse(isinstance(testCase1.get_favorite_dishes(),str))
    def test_4(self):
        self.assertFalse(isinstance(testCase1,str))
    def test_5(self):
        self.assertIsNotNone(testCase1.get_favorite_dishes())
    def test_6(self):
        self.assertIsNotNone(testCase1.avoid_dishes())
    def test_7(self):
        self.assertIsInstance(testCase1,Customer)
    def test_8(self):
        self.assertIsInstance(testCase2,Dish)
    def test_9(self):
        self.assertIsInstance(testCase3,db_system)


if __name__ == '__main__':
    unittest.main()
