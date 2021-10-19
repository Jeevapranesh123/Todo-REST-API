from fastapi import APIRouter,Response,status
from pydantic import BaseModel
from apimain.Lib.Signup_class import *
from apimain.Lib.Auth_class import *

router = APIRouter()

class signup(BaseModel):
    name:str
    email:str
    password:str

@router.post('/auth/signup')
def signup(data:signup,response:Response):
    a=Signup()
    x=a.createuser(data.name.lower(),data.email.lower(),data.password.lower())
    if x:
        data={
            'Message': 'Signup Success',
            'Username': data.name,
            'Email': data.email,

        }
        response.status_code=200
        return data
    
    else:
        data = {
            'Error':'Signup Failure',
            'Message':'Email already exists',
        }
        response.status_code=409

        return data

class Login(BaseModel):
    email:str
    password:str


@router.post('/auth/login')
def login(data:Login,response:Response):
    try:
        a=Auth(data.email.lower(),data.password.lower())
        data={
                'Message':'login Success',
                'Data':a.getdata(),
        }
        response.status_code=200
        return data
    except Exception as e:
        data={
                'Error':str(e),
            }
        response.status_code=401
        return data

class Isvalid(BaseModel):
    token:str
    
@router.post('/auth/isvalid')
def isvalid(data:Isvalid,response:Response):
    a=Auth(data.token)
    if a.authenticate():
        data={
            'Valid': True,
            'Valid_for':a.valid_for_token()
        }
        response.status_code=200
        return data
    else:
        data={
            'Error':'Invalid Token'
        }
        response.status_code=200
        return data

@router.get('/test')
def test(response:Response):
    print('Hello')
    a=Signup().test()
    return {
        'Message':a['Message'],
        'Api_Status':a['Api_Status']
    }
