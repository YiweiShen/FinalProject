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


if __name__ == '__main__':
    # To reset the dish collection in the database, please run the current file by itself. 
    dish_db = MongoClient().project_db.dishes
    dish_db.drop()
    posts = [
        { "_id": 1,
          "dish_id": "1",
          "name": "Chicken Soup",
          "rating": 4,
          "type": "Soup",
          "ingredients": "chicken",
          "description": "liquid food prepared by cooking meat, poultry with seasonings in water, stock, milk, or some other liquid medium", 
          "preparation_time": 20,
          "available_date_start": "22-07-2020",
          "available_date_end": "01-12-2020",
          "modify_date": "21-07-2020",
        },
        { "_id": 2,
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
        },
        { "_id": 3,
          "dish_id": "3",
          "name": "Beef Steak",
          "rating": 4,
          "type": "Main Dish",
          "ingredients": "Beef",
          "description": "An American cutlet like dish with large and tender chicken pieces marinated well, bursting with flavours of spices", 
          "preparation_time": 120,
          "available_date_start": "01-05-2020",
          "available_date_end": "31-12-2020",
          "modify_date": "30-04-2020",
        },
        { "_id":4,
          "dish_id": "4",
          "name": "Lobster tail",
          "rating": 5,
          "type": "Main Dish",
          "ingredients": "Lobster",
          "description": "decadent dinner made with large lobster tails smothered with a buttery garlic herb sauce then broiled under high heat", 
          "preparation_time": 60,
          "available_date_start": "01-07-2020",
          "available_date_end": "31-12-2020",
          "modify_date": "30-06-2020",
        },
    ]
    dish_db.insert_many(posts)
