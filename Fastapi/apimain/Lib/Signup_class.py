import pymongo
import json


client=pymongo.MongoClient('localhost')
db=client.Intern
Users=db.Users


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




