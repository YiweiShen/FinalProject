import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["restaurant"]

collection = mydb["customers"]
   
customerlist = [
  { "_id": 1,"customer_id":1, "first_name": "John","last_name":"Abraham","gender":"Male", "address": "Highway 37","email":"john@gmail.com","phone":"416-1234751","favorite_dishes":2,"registration_date":"12-07-2020","allergy_ingredient":"Peanut"},
  { "_id": 2, "customer_id":2, "first_name": "Amy","last_name":"James","gender":"Female", "address": "42 Avenue","email":"amy@gmail.com","phone":"416-7684753","favorite_dishes":1,"registration_date":"21-07-2020","allergy_ingredient":"Lobster"},
  { "_id": 3, "customer_id":3, "first_name": "Ben","last_name":"Tison","gender":"Male", "address": "52 Dennett","email":"ben@gmail.com","phone":"419-7682354","favorite_dishes":3,"registration_date":"01-08-2020","allergy_ingredient":""}
]

collection = mydb["menu"]

menulist = [

    { "_id":1,"dish_id":1,"name":"Chicken Soup","rating":4,"type":"Soup","ingredients":"chicken","description":"liquid food prepared by cooking meat, poultry with seasonings in water, stock, milk, or some other liquid medium", "prepration-time":20,"available_date_start":"22-07-2020","available_date_end":"01-12-2020","modify_date":"21-07-2020"},
    { "_id":2,"dish_id":2,"name":"Chicken curry","rating":5,"type":"Main Dish","ingredients":"Tender Chicken","description":"onion- and tomato-based sauce, flavoured with ginger, garlic, tomato puree, chilli peppers and a variety of spices, often including turmeric, cumin, coriander, cinnamon, and cardamom", "prepration-time":40,"available_date_start":"01-01-2020","available_date_end":"31-12-2020","modify_date":"01-01-2020"},
    { "_id":3,"dish_id":3,"name":"Beef Steak","rating":4,"type":"Main Dish","ingredients":"Beef","description":"An American cutlet like dish with large and tender chicken pieces marinated well, bursting with flavours of spices", "prepration-time":120,"available_date_start":"01-05-2020","available_date_end":"31-12-2020","modify_date":"30-04-2020"},
    { "_id":4,"dish_id":4,"name":"Lobster tail","rating":5,"type":"Main Dish","ingredients":"Lobster","description":"decadent dinner made with large lobster tails smothered with a buttery garlic herb sauce then broiled under high heat", "prepration-time":60,"available_date_start":"01-07-2020","available_date_end":"31-12-2020","modify_date":"30-06-2020"}

]

y = collection.insert_many(menulist)




