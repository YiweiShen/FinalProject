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
        customer_str = f'Customer ID: {self.customer_id}\n' + 
                       f'First Name: {self.first_name}\n' +
                       f'Last Name: {self.last_name}\n' +
                       f'Gender: {self.gender}\n' +
                       f'Address: {self.address}\n' +
                       f'Email: {self.eamil}\n' +
                       f'Phone: {self.phone}\n' +
                       f'Favarote Dishes: {self.get_favorite_dishes()}\n' +
                       f'Registration Date: {self.registration_date}\n' +
                       f'Allergy to: {self.allergy_ingredient}\n' +
                       f'Avoid Dishes: {self.avoid_dishes()}\n' +
        return customer_str

    def get_favorite_dishes(self):
        if len(self.favorite_dishes) == 0:
            return f''
        else:
            favorite_dishes = []
            for i in self.favorite_dishes:
                r = self.dish_db.find_one({'dish_id': i})
                favorite_dishes.append(r['name'])
            return favorite_dishes
    
    def avoid_dishes(self):
        dishes = self.dish_db.find()
        dish_to_avoid = []
        for i in self.allergy_ingredient:
            for j in dishes:
                if i in j['ingredients']:
                    dish_to_avoid.append({j['dish_id']:j['name']})