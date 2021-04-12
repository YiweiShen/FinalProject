#!/usr/bin/env python3

import datetime
from pymongo import MongoClient

class Customer():
    
    def __init__(self):
        self.customers = MongoClient().project_db.customers

    # CREATE

    def create_one_line(self, one_record):
        self.customers.insert_one(one_record)

    def create_multiple_lines(self, record_list):
        self.customers.insert_many(record_list)

    # READ

    def read_one_line(self, match_dict):
        match = self.customers.find_one(match_dict)
        return match

    def read_multiple_lines(self, match_dict):
        match = self.customers.find_many(match_dict)
        return match

    # UPDATE

    def update_one_line(self, match_dict, update_dict):
        self.customers.update_one(match_dict, {'$set': update_dict})

    def update_multiple_lines(self, match_dict, update_dict):
        self.customers.update_many(match_dict, {'$set': update_dict})

    # DELETE

    def delete_one_line(self, match_dict):
        self.customers.delete_one(match_dict)

    def delete_multiple_lines(self, match_dict):
        self.customers.delete_many(match_dict)


if __name__ == '__main__':
    c = Customer()
