#!/usr/bin/env python3
# Dish class

from pymongo import MongoClient

class Dish():
    
    def __init__(self, dish_dict):
        self.dish_id = dish_dict['dish_id']
        self.name = dish_dict['name']
        self.rating = dish_dict['rating'] # 1-5, 5 is highest
        self.type = dish_dict['type'] # Main dish, Breakfast, Salad, Dessert, Side Dish
        self.ingredients = dish_dict['ingredients']
        self.description = dish_dict['description']
        self.preparation_time = dish_dict['preparation_time'] # cook time in minutes
        self.available_date_start = dish_dict['available_date_start'] # the date when the dish is available in the restaurant
        self.available_date_end = dish_dict['available_date_end'] # the date when the dish is no longer available in the restaurant
        self.modify_date = dish_dict['modify_date'] # the date that the dish item is last modified