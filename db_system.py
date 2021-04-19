#!/usr/bin/env python3

import sys
from pymongo import MongoClient
from Customer import Customer


class db_system:
    def __init__(self):
        self.customer_db = MongoClient().project_db.customers

    def system_run(self):
        while True:
            self.menu()
            choice = input('Please choose: ')
            if choice == '1':
                self.add_new_customer()
            elif choice == '2':
                self.update_customer()
            elif choice == '3':
                self.search_customer()
            elif choice == '4':
                self.delete_customer()
            elif choice == '5':
                self.exit()
            elif choice == '6':
                self.reset()
            else:
                print('\x1b[6;33;41m' + 'Please choose between 1 and 6.' + '\x1b[0m')

    # CREATE
    def add_new_customer(self):
        print('--------- Add new customer ----------')
        first_name = input("What's the first name: ")
        last_name = input("What's the last name: ")
        customer_id = input("What's the assigned customer ID: ")
        one_record = {'customer_id':customer_id, 'first_name':first_name, 'last_name':last_name}
        c = self.customer_db.insert_one(one_record)
        print(c)
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
        print('-------------------------------------')

    # UPDATE
    def update_customer(self):
        print('---------- Update customer ----------')
        customer_id_to_update = input('Please enter the Customer ID you want to update: ')
        print('Which field you want to update: (Default last name)')
        print('1. First Name. 2. Last Name.')
        choice = input('Please choose: ')
        if choice == '1':
            update_field = 'first_name'
            print('Update the first name')
        else:
            update = 'last_name'
            print('Update the last name')

        update_to = input('Update as: ')
        u = self.customer_db.update_one({'customer_id': customer_id_to_update}, {'$set': {update_field: update_to}})
        print(u)
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
        print('-------------------------------------')

    # READ
    def search_customer(self):
        print('------- Search for a customer -------')
        print('Search by: (Default Customer ID)')
        print('1. Customer ID. 2. First Name. 3. Last Name.')
        choice = input('Please choose: ')
        if choice == '2':
            search_field = 'first_name'
            print('Search by the first name')
        elif choice == '3':
            search_field = 'last_name'
            print('Search by the last name')
        else:
            search_field = 'customer_id'
            print('Search by the customer ID')
        match = input('Search: ')
        r = self.customer_db.find_one({search_field: match})
        print(r)
        if r:
            print('Record found.')
            print(f"\033[93mCustomer ID: {r['customer_id']}\033[0m")
            print(f"\033[93mFirst Name: {r['first_name']}\033[0m")
            print(f"\033[93mLast Name: {r['last_name']}\033[0m")
        else:
            print('\x1b[6;33;41m' + 'Sorry, no record found.' + '\x1b[0m')
        print('-------------------------------------')

    # DELETE
    def delete_customer(self):
        print('---------- Delete customer ----------')
        customer_id_to_delete = input('Please enter the Customer ID you want to delete: ')
        d = self.customer_db.delete_one({'customer_id': customer_id_to_delete})
        print(d)
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
        print('-------------------------------------')


    def exit(self):
        print('Thank you for using the customer database.')
        sys.exit(0)


    def menu(self):
        print('--------- Customer Database ---------')
        print('1. Add new customer.')
        print('2. Update customer.')
        print('3. Search for a customer.')
        print('4. Delete customer.')
        print('5. Exit.')
        print('6. Reset Database.')
        print('-------------------------------------')


    def reset(self):
        print(f"\033[91m----------- Database Reset ----------\033[0m")
        confirm = input('Please enter "RESET" to proceed (in capital letters): ')
        if confirm == 'RESET':
            self.customer_db.drop()
            print('\x1b[6;30;42m' + 'Success! Database is reset.' + '\x1b[0m')
        else:
            print('\x1b[6;33;41m' + 'No action taken.' + '\x1b[0m')
        print('-------------------------------------')


if __name__ == '__main__':
    db_new = db_system()
    db_new.system_run()