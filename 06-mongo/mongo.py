#Team OrangeOranges: Dennis Chen & Simon Tsui
#SoftDev pd7
#K #06: Yummy Mongo Py
#2/28/19
import pymongo
from pymongo import MongoClient
client = MongoClient()
SERVER_ADDR = "204.48.19.94"
connection = MongoClient(SERVER_ADDR)
db = connection.test
collection = db.restaurants
def rBoroughs(bor):
    restaurants = []
    #finds restaurants that have the same borough as the parameter
    for restaurant in collection.find({"borough": bor}):
        restaurants.append(restaurant["name"])
    print(restaurants)
    return restaurants
rBoroughs("Bronx")
def rZip(zip):
    zips = []
    #finds restaurants that have the same zipcode inside an address dictionary as the parameter
    for rest in collection.find({"address.zipcode" : zip}):
        zips.append(rest['name'])
    print(zips)
    return zips
rZip("10462")
def zipGrade(zip,grade):
    rests = []
    #finds restaurants that have the same zipcode and a grade inside a list of dictionaries of grades as the parameters
    for rest in collection.find( { '$and': [{"address.zipcode": zip},{"grades.1.grade" : grade}]}):
        rests.append(rest['name'])
    print(rests)
    return rests
zipGrade("10462","A")
def zipScore(zip,score):
    rests = []
    #finds restaurants that have the same zipcode and a score less than the score given in the parameter
    for rest in collection.find( { '$and': [{"address.zipcode": zip}, {"grades.1.score" : {'$lt' : score}}]}):
        rests.append(rest['name'])
    print(rests)
    return rests
zipScore('10462',6)
def rCat(cat, bor, score):
    rests = []
    #finds restaurants that have a certain cuisine in a certain borough with a score below what's given
    for rest in collection.find( { "$and": [{"cuisine": cat}, {"borough": bor}, {"grades.1.score": { "$lt" : score}}]}):
        rests.append(rest['name'])
    print(rests)
    return rests
rCat("American", "Bronx", 20)
print(collection.find_one())
