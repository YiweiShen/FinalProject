#!/usr/bin/env python3

import sys
import datetime
from pymongo import MongoClient
from Customer import Customer


class db_system:
    def __init__(self):
        # set the database
        try:
            self.customer_db = MongoClient().project_db.customers
        except:
            print('\x1b[6;33;41m' + 'Fail to connect to the customer database.' + '\x1b[0m')
        
    def system_run(self):
        # the choice on the main menu
        while True:
            self.menu()
            choice = input('Please choose: ')
            if choice == '1':
                self.show_all_customer()
            elif choice == '2':
                self.add_new_customer()
            elif choice == '3':
                self.search_customer()
            elif choice == '4':
                self.update_customer()
            elif choice == '5':
                self.delete_customer()
            elif choice == '6':
                self.reset()
            elif choice == '7':
                self.exit()
            else:
                print('\x1b[6;33;41m' + 'Please choose between 1 and 7.' + '\x1b[0m')


    def show_all_customer(self):
        # Show customer ID with names for all customers.
        print('----------- All customer ------------')
        try:
            customer_num = self.customer_db.estimated_document_count()
        except:
            customer_num = 0
        if customer_num == 0:
            print('\x1b[6;33;41m' + 'No customer in the database.' + '\x1b[0m')
        else:
            for i in self.customer_db.find():
                print(f"\033[94mNo.{i['customer_id']} {i['first_name']} {i['last_name']}\033[0m")
        print('-------------------------------------')


    def add_new_customer(self):
        # Create a new customer in the database.
        print('--------- Add new customer ----------')
        try:
            customer_id_list = [0]
            for i in self.customer_db.find():
                customer_id_list.append(int(i['customer_id']))
            customer_id = str(max(customer_id_list)+1)
        except:
            customer_id = '1'

        first_name = input("What's the first name: ")
        last_name = input("What's the last name: ")
        gender = input("What's the gender: ")
        address = input("What's the address: ")
        email = input("What's the email: ")
        phone = input("What's the phone number: ")
        registration_date = datetime.date.today().strftime('%d-%m-%Y')
        favorite_dishes = self.input_favorite_dishes()
        allergy_ingredient = self.input_allergy_ingredient()

        one_record = {'customer_id':customer_id, 
                      'first_name':first_name, 
                      'last_name':last_name,
                      'gender': gender,
                      'address': address,
                      'email': email,
                      'phone': phone,
                      'favorite_dishes': favorite_dishes,
                      'registration_date': registration_date,
                      'allergy_ingredient': allergy_ingredient,
                     }
        try:
            c = self.customer_db.insert_one(one_record)
            print('\x1b[6;30;42m' + 'New customer created!' + '\x1b[0m')
        except:
            print('\x1b[6;33;41m' + 'Fail to create new customer.' + '\x1b[0m')
        print('-------------------------------------')


    def update_customer(self):
        # Update customer for different properties.
        print('---------- Update customer ----------')
        customer_id_to_update = input('Please enter the Customer ID you want to update: ')
        try:
            r = self.customer_db.find_one({'customer_id': customer_id_to_update})
        except:
            r = None
        if r:
            print('Which field you want to update: (Default first name)')
            print('1.First Name. 2.Last Name. 3.Gender. 4.Address.')
            print('5.Email. 6.Phone. 7.Favorite Dishes. 8.Allergy Ingredient.')
            choice = input('Please choose: ')
            if choice == '2':
                update_field = 'last_name'
                print('Update the last name')
                update_to = input('Update to: ')
            elif choice == '3':
                update_field = 'gender'
                print('Update the gender')
                update_to = input('Update to: ')
            elif choice == '4':
                update_field = 'address'
                print('Update the address')
                update_to = input('Update to: ')
            elif choice == '5':
                update_field = 'email'
                print('Update the email')
                update_to = input('Update to: ')
            elif choice == '6':
                update_field = 'phone'
                print('Update the phone number')
                update_to = input('Update to: ')
            elif choice == '7':
                update_field = 'favorite_dishes'
                print('Update the favorite dishes')
                update_to = self.input_favorite_dishes()
            elif choice == '8':
                update_field = 'allergy_ingredient'
                print('Update the allergy ingredient')
                update_to = self.input_allergy_ingredient()
            else:
                update_field = 'first_name'
                print('Update the first name')
                update_to = input('Update to: ')

            try:
                u = self.customer_db.update_one({'customer_id': customer_id_to_update}, {'$set': {update_field: update_to}})
                print('\x1b[6;30;42m' + 'Customer info updated!' + '\x1b[0m')
            except:
                print('\x1b[6;33;41m' + 'Fail to update customer info.' + '\x1b[0m')
        else:
            print('\x1b[6;33;41m' + 'Sorry, customer not found.' + '\x1b[0m')
        print('-------------------------------------')


    def search_customer(self):
        # Search in the database for a customer by different properties of customer.
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
        try:
            r = self.customer_db.find_one({search_field: match})
        except:
            r = None
        if r:
            print('Record found.')
            match_customer = Customer(r)
            print(f"\033[94m{match_customer}\033[0m")
        else:
            print('\x1b[6;33;41m' + 'Sorry, no record found.' + '\x1b[0m')
        print('-------------------------------------')


    def delete_customer(self):
        # Find one customer using customer ID, and delete it.
        print('---------- Delete customer ----------')
        customer_id_to_delete = input('Please enter the Customer ID you want to delete: ')
        try:
            r = self.customer_db.find_one({'customer_id': customer_id_to_delete})
        except:
            r = None
        if r:
            try:
                d = self.customer_db.delete_one({'customer_id': customer_id_to_delete})
                print('\x1b[6;30;42m' + 'Customer deleted!' + '\x1b[0m')
            except:
                print('\x1b[6;33;41m' + 'Fail to delete the customer.' + '\x1b[0m')
        else:
            print('\x1b[6;33;41m' + 'Sorry, customer not found.' + '\x1b[0m')
        print('-------------------------------------')


    def exit(self):
        # Exit of the app.
        print('Program Exit...')
        print('\x1b[6;30;42m' + 'Thank you for using the customer database.' + '\x1b[0m')
        sys.exit(0)


    def menu(self):
        # Show the main menu of the app.
        print('--------- Customer Database ---------')
        print('1. Show all customer.')
        print('2. Add new customer.')
        print('3. Search for a customer.')
        print('4. Update customer.')
        print('5. Delete customer.')
        print('6. Reset Database.')
        print('7. Exit.')
        print('-------------------------------------')


    def reset(self):
        # Database reset: clean up the customer database.
        print(f"\033[91m----------- Database Reset ----------\033[0m")
        confirm = input('Please enter "RESET" to proceed (in capital letters): ')
        if confirm == 'RESET':
            self.customer_db.drop()
            print('\x1b[6;30;42m' + 'Success! Database has been reset.' + '\x1b[0m')
        else:
            print('\x1b[6;33;41m' + 'No action taken.' + '\x1b[0m')
        print('-------------------------------------')

    
    def input_favorite_dishes(self):
        # use loop to collect the list of favorate dishes
        favorite_dishes_num = input("How many favorite dishes: ")
        favorite_dishes = []
        for i in range(int(favorite_dishes_num)):
            favorite_dish = input(f"No.{i+1} What's the favorite dishes: ")
            favorite_dishes.append(favorite_dish)
        return favorite_dishes


    def input_allergy_ingredient(self):
        # use loop to collect the list of allergy ingredient
        allergy_ingredient_num = input("How many allergy ingredient: ")
        allergy_ingredient = []
        for i in range(int(allergy_ingredient_num)):
            allergy_ingredient_item = input(f"No.{i+1} What's the allergy ingredient: ")
            allergy_ingredient.append(allergy_ingredient_item)
        return allergy_ingredient


if __name__ == '__main__':
    db_new = db_system()
    db_new.system_run()
