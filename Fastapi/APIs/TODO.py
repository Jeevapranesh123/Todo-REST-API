from fastapi import APIRouter,Response,status,Header,Request
from typing import Optional
from pydantic import BaseModel
from Lib.func import *
from Lib.Signup_class import *
from Lib.Auth_class import *
from Lib.Todo_class import *

todoapi = APIRouter()

class AddTasks(BaseModel):
    taskname :str
    due_date :Optional[int] = None

class CompleteTask(BaseModel):
    taskname:str

class DeleteTask(BaseModel):
    taskname:str

class UpdateTask(BaseModel):
    taskname:str
    duedate:int

class UpdateTaskbyid(BaseModel):
    duedate:int

@todoapi.post('/todo/task/add')
def addtask(data:AddTasks,request:Request,response:Response):
    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data
    if is_valid(token):
        try:

            a=TODO().add_task(data.taskname.lower(),token,data.due_date)

            if a:
                data={
                    "Success":1,
                    "Message":"Task Added Succesfully",
                    "data":{
                        "Task_id":a['_id'],
                        "Task_Owner":a['Task_Owner'],
                        "Email":a['Email'],
                        "Task_Name":a['Task_Name'],
                        "due_date":a['due_date'],
                        "completed": a['completed'],
                    }
                }
                response.status_code=200
                return data
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data


@todoapi.get('/todo/tasks')
def get_todo_tasks(request:Request,response:Response):
    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        try:
            a=TODO().get_tasks(token)
            data={
                "Success":1,
                "data":a
            }
            response.status_code=200
            return data
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data


@todoapi.get('/todo/task/{task_id}')
def get_one_task(task_id:int,request:Request,response:Response):


    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        a=TODO().get_task(token,task_id)
        data={
            "Success":1,
            "data":a
        }
        response.status_code=200
        return data
    
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data


@todoapi.get('/todo/tasks/completed')
def get_completed_task(request:Request,response:Response):
    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        try:

            a=TODO().get_task_complete(token)
            data={
                "Success":1,
                "data":a
            }
            response.status_code=200
            return data
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data
        

@todoapi.put('/todo/task/complete')
def update_complete_task(data:CompleteTask,request:Request,response:Response):
    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        try:
            a=TODO().complete_task(token,data.taskname.lower())
            data={
                "Success":1,
                "Message":"Task Completed"
            }
            response.status_code=200
            return data
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data


@todoapi.put('/todo/task/complete/{id}')
def update_complete_task_by_id(id:int,request:Request,response:Response):

    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        try:
            a=TODO().complete_task(token,id=id)
            data={
                "Success":1,
                "Message":"Task Completed"
            }
            response.status_code=200
            return data
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data


@todoapi.delete('/todo/task/delete')
def delete_task_by_name(data:DeleteTask,request:Request,response:Response):
    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        try:
            a=TODO().archive_task(token,data.taskname.lower())
            data={
                "Success":1,
                "Message":"Task deleted successfully",
                "Task_id":a[1]
            }
            response.status_code=200
            return data
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data
        

@todoapi.delete('/todo/task/delete/{id}')
def delete_task_by_name(id:int,request:Request,response:Response):
    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        try:
            a=TODO().archive_task(token,id=id)
            data={
                "Success":1,
                "Message":"Task deleted successfully",
                "Task_id":a[1]
            }
            response.status_code=200
            return data
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data


@todoapi.put('/todo/task/update/duedate')
def update_task_duedate_by_task_name(data:UpdateTask,request:Request,response:Response):
    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        try:

            a=TODO().update_due_date(token,data.duedate,data.taskname.lower())
            data={
                "Success":1,
                "Message":"Due Date Updated",
                "Task_id":a[1]
            }
            response.status_code=200
            return data
        
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data


@todoapi.put('/todo/task/update/duedate/{id}')
def update_task_duedate_by_task_id(id:int,data:UpdateTaskbyid,request:Request,response:Response):
    token=request.headers.get('Authorization')
    if token is None:
        data={
            "Error":"Unauthorized"
        }

        response.status_code=401
        return data

    if is_valid(token):
        try:

            a=TODO().update_due_date(token,data.duedate,id=id)
            data={
                "Success":1,
                "Message":"Due Date Updated",
                "Task_id":a[1]
            }
            response.status_code=200
            return data
        
        except Exception as e:
            data={
                "Error":str(e)
            }
            response.status_code=400
            return data
    else:
        data={
            "Error":"Unauthorized"
        }
        response.status_code=401
        return data