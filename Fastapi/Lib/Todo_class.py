import re
from bson.py3compat import reraise
import pymongo
import json
import pprint
import time
client=pymongo.MongoClient('localhost')
db=client.Intern
Session=db.Session
Users=db.Users
Tasks=db.Tasks

class TODO:

    def __init__(self):
        pass

    def add_task(self, taskname,token,due_date=None):
        
        token=token.split(' ')[1]
        print(token)
        x=Session.find_one({'token':token})
        name=x['username']
        email=x['email']

        a=Tasks.find_one({'Task_Name':taskname,'completed':False,'Task_Owner':name})
        if a is None:
            max=0
            m=Tasks.find()
            for i in m:
                if i['_id']>max:
                    max=i['_id']

            data={
                "_id":max+1,
                "Task_Owner":name,
                "Email":email,
                "Task_Name": taskname,
                "due_date":due_date,
                "completed": False,
                "archived": False,
            }
            Tasks.insert_one(data)
            return data
        else:
            raise Exception("Task Already Exist")

    def get_tasks(self,token):

        token=token.split(' ')[1]
        x=Session.find_one({'token':token})
        if x is None:
            raise Exception('Session not found')
        name=x['username']

        a=Tasks.find()
        data=[]
        for i in a:
            if i['Task_Owner']==name:
                data.append(i)

        return data

    def get_task(self,token,id):
        token=token.split(' ')[1]
        x=Session.find_one({'token':token})
        if x is None:
            raise Exception('Session not found')
        name=x['username']

        a=Tasks.find_one({'_id':id,'Task_Owner':name})
        if a:
            return a
        else:
            return {}

    def get_task_complete(self,token):
        token=token.split(' ')[1]
        x=Session.find_one({'token':token})
        if x is None:
            raise Exception('Session not found')
        name=x['username']

        a=Tasks.find()
        data=[]
        for i in a:
            if i['Task_Owner']==name:
                if i['completed']==True:
                    data.append(i)
        return data

    def complete_task(self,token,taskname=None,id=None):
        token=token.split(' ')[1]
        x=Session.find_one({'token':token})
        if x is None:
            raise Exception('Session not found')
        name=x['username']

        if id is None:

            a=Tasks.find_one({'Task_Owner':name,'Task_Name':taskname})
            if a:
                print(a)
                if a['completed']==False:
                    filter = { 'Task_Name':taskname}
                    newvalues = { "$set": { 'completed':True } }
                    Tasks.update_one(filter,newvalues)
                    return [True,a['_id']]
                else:
                    raise Exception('Task Already Completed')
            else:
                raise Exception('Task Not Found')

        else:
            a=Tasks.find_one({'Task_Owner':name,'_id':id})
            if a:
                print(a)
                if a['completed']==False:
                    filter = { '_id':id}
                    newvalues = { "$set": { 'completed':True } }
                    Tasks.update_one(filter,newvalues)
                    return [True,a['_id']]
                else:
                    raise Exception('Task Already Completed')
            else:
                raise Exception('Task Not Found')

    def archive_task(self,token,taskname=None,id=None):
        token=token.split(' ')[1]
        x=Session.find_one({'token':token})
        if x is None:
            raise Exception('Session not found')
        name=x['username']

        if id is None:

            a=Tasks.find_one({'Task_Owner':name,'Task_Name':taskname})
            if a:
                print(a)
                if a['archived']==False:
                    filter = { 'Task_Name':taskname}
                    newvalues = { "$set": { 'archived':True } }
                    Tasks.update_one(filter,newvalues)
                    return [True,a['_id']]
                else:
                    raise Exception('Task Already Archived')
            else:
                raise Exception('Task Not Found')

        else:
            a=Tasks.find_one({'Task_Owner':name,'_id':id})
            if a:
                print(a)
                if a['archived']==False:
                    filter = { '_id':id}
                    newvalues = { "$set": { 'archived':True } }
                    Tasks.update_one(filter,newvalues)
                    return [True,a['_id']]
                else:
                    raise Exception('Task Already Archived')
            else:
                raise Exception('Task Not Found')


    def update_due_date(self,token,due_date,taskname=None,id=None):
        token=token.split(' ')[1]
        x=Session.find_one({'token':token})
        if x is None:
            raise Exception('Session not found')
        name=x['username']

        if id is None:

            a=Tasks.find_one({'Task_Owner':name,'Task_Name':taskname})
            if a:
                print(a)
                if due_date>int(time.time()):
                    filter = { 'Task_Name':taskname}
                    newvalues = { "$set": { 'due_date':due_date } }
                    Tasks.update_one(filter,newvalues)
                    return [True,a['_id']]
                else:
                    raise Exception('Due Date Invalid')
            else:
                raise Exception('Task Not Found')

        else:
            a=Tasks.find_one({'Task_Owner':name,'_id':id})
            if a:
                print(a)
                if due_date>int(time.time()):
                    filter = { '_id':id}
                    newvalues = { "$set": { 'due_date':due_date } }
                    Tasks.update_one(filter,newvalues)
                    return [True,a['_id']]
                else:
                    raise Exception('Due Date Invalid')
            else:
                raise Exception('Task Not Found')







# print(TODO().get_task('Bearer 0f39083d8232f89fd1254936184050a9',10))
    

