import pymongo
import json
from apimain.Lib.client import *


# client=pymongo.MongoClient('localhost')
db=client.Intern
Users=db.Users
Home=db.Home


class Signup:

    def __init__(self):
        pass

    def createuser(self, username,email, password):
        data = {
            'username':username.lower(),
            'email': email,
            'Password': password,
        }
        a = Users.find()
        for i in a:
            # print(i)
            if i['email'] == email:
                print('Email already exists')
                return False
        else:
            Users.insert_one(data)

            return True

    def verifytoken(self,username,password):
        pass

    def test(self):
        a=Home.find_one({'Message':'Hurray you are now connected to MongoDB and Your API is up. Go Ahead and Use it :)'})
        if a is not None:
            return a
        else:
            data={
                "Message":"Hurray you are now connected to MongoDB",
                "Api_Status":"Up",
            }
            a=Home.insert_one(data)
            x=Home.find_one({'Message':'Hurray you are now connected to MongoDB'})
            return x






