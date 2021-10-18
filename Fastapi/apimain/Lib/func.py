from apimain.Lib.Auth_class import Auth
import pymongo

client =pymongo.MongoClient('localhost')
db = client.Intern
Users = db.Users
Sessions = db.Sessions
Task = db.Task

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
