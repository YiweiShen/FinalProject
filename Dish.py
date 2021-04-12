#!/usr/bin/env python3

import datetime
from pymongo import MongoClient

class Dish():
    
    def __init__(self):
        self.dishes = MongoClient().project_db.dishes

    # CREATE

    def create_one_line(self, one_record):
        self.dishes.insert_one(one_record)

    def create_multiple_lines(self, record_list):
        self.dishes.insert_many(record_list)

    # READ

    def read_one_line(self, match_dict):
        match = self.dishes.find_one(match_dict)
        return match

    def read_multiple_lines(self, match_dict):
        match = self.dishes.find_many(match_dict)
        return match

    # UPDATE

    def update_one_line(self, match_dict, update_dict):
        self.dishes.update_one(match_dict, {'$set': update_dict})

    def update_multiple_lines(self, match_dict, update_dict):
        self.dishes.update_many(match_dict, {'$set': update_dict})

    # DELETE

    def delete_one_line(self, match_dict):
        self.dishes.delete_one(match_dict)

    def delete_multiple_lines(self, match_dict):
        self.dishes.delete_many(match_dict)


if __name__ == '__main__':
    d = Dish()
