#!/usr/bin/env python3
# Customer class

from Dish import Dish
from pymongo import MongoClient

class Customer():
    
    def __init__(self, customer_dict):
        self.customer_id = customer_dict['customer_id']
        self.first_name = customer_dict['first_name']
        self.last_name = customer_dict['last_name']
        self.gender = customer_dict['gender']
        self.address = customer_dict['address']
        self.email = customer_dict['email']
        self.phone = customer_dict['phone']
        self.favorite_dishes = customer_dict['favorite_dishes'] # list of dish ID that are favorites of the customer
        self.registration_date = customer_dict['registration_date']
        self.allergy_ingredient = customer_dict['allergy_ingredient']
        self.dish_db = MongoClient().project_db.dishes


    def __str__(self):
        customer_str = f'Customer ID: {self.customer_id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nGender: {self.gender}\nAddress: {self.address}\nEmail: {self.email}\nPhone: {self.phone}\nFavarote Dishes: {self.get_favorite_dishes()}\nRegistration Date: {self.registration_date}\nAllergy to: {self.allergy_ingredient}\nAvoid Dishes: {self.avoid_dishes()}\n'
        return customer_str


    def get_favorite_dishes(self):
        if len(self.favorite_dishes) == 0:
            return f''
        else:
            favorite_dish_list = []
            for i in self.favorite_dishes:
                r = self.dish_db.find_one({'dish_id': i})
                favorite_dish_list.append(r['name'])
            return favorite_dish_list


    def avoid_dishes(self):
        dishes = self.dish_db.find()
        dish_to_avoid = []
        for i in self.allergy_ingredient:
            for j in dishes:
                if i in j['ingredients']:
                    dish_to_avoid.append(j['name'])
        return dish_to_avoid


if __name__ == '__main__':
    # To reset the customer collection in the database, please run the current file by itself.
    customer_db = MongoClient().project_db.customers
    customer_db.drop()
    posts = [
        { "_id": 1,
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
        },
        { "_id": 2, 
          "customer_id": "2", 
          "first_name": "Amy",
          "last_name": "James",
          "gender": "Female", 
          "address": "42 Avenue",
          "email": "amy@gmail.com",
          "phone": "416-7684753",
          "favorite_dishes": ["1"],
          "registration_date": "21-07-2020",
          "allergy_ingredient": ["Lobster"],
        },
        { "_id": 3, 
          "customer_id": "3", 
          "first_name": "Ben",
          "last_name": "Tison",
          "gender": "Male", 
          "address": "52 Dennett",
          "email": "ben@gmail.com",
          "phone": "419-7682354",
          "favorite_dishes": ["3"],
          "registration_date": "01-08-2020",
          "allergy_ingredient": [],
        },
    ]
    customer_db.insert_many(posts)
