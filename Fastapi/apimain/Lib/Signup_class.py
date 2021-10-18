import pymongo
import json
# from apimain.Lib.client import *


client=pymongo.MongoClient('localhost')
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

        a=Home.find_one({"Message":"Hello"})
        if a:
            return a
        else:
            data={
                "Message":"Hello",
                "Mongodb":"Connected"
            }
            a=Home.insert_one(data)

            x=Home.find_one({'Message':'Hello'})
            return x






