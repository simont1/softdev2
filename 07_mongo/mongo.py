#Team cookie: Angela Tom & Simon Tsui
#SoftDev pd7
#K #06: Yummy Mongo Py
#2/28/19

#We chose the historical events database which includes the dates and description of recorded events
#Raw data source:http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en

import pymongo
from pymongo import MongoClient
client = MongoClient()
SERVER_ADDR = "142.93.207.20"
connection = MongoClient(SERVER_ADDR)
db = connection.historicalevents
collection = db.history
def findDate(year):
    results = []
    print("Hi")
    #returns events that occurred in that year
    for event in collection.find({"date": year}):
        print(event)
        results.append(event["description"])
    return results
print(findDate("-40"))
def findCat(cat):
    results = []
    #returns events that occurred in that category
    for event in collection.find({"category2": cat}):
        results.append(event["description"])
    return results
print(findCat("Roman Republic"))
