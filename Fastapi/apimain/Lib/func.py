from apimain.Lib.Auth_class import Auth
import pymongo
from apimain.Lib.client import *

# client =pymongo.MongoClient('localhost')
db = client.Intern
Users = db.Users
Sessions = db.Sessions
Task = db.Task
Home = db.Home

def mysqlclean(a):
    return a


def is_valid(token):

    x=token.split(' ')
    if token:
        a=Auth(x[1])
    else:
        return {'Error':'No data Input'},400
    if a.authenticate():
        return True
    else:
        return False

def connect():
    a=Home.find_one({"Message":"Hurray you are now connected to MongoDB and Your API is up. Go Ahead and Use it :)"})

    if a:
        return a
    
    else:
        Home.insert_one({"Message":"Hurray you are now connected to MongoDB and Your API is up. Go Ahead and Use it :)"})

        a=Home.find_one({"Message":"Hurray you are now connected to MongoDB and Your API is up. Go Ahead and Use it :)"})

        return a
