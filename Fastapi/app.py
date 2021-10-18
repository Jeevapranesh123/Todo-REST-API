from apimain.Lib.func import connect
from fastapi import FastAPI
from pydantic import BaseModel
from apimain.APIs.Auth import router
from apimain.APIs.TODO import todoapi
from apimain.Lib.client import *


app=FastAPI()


@app.get('/')
def home():
    return {"Details":"REST API's for a TODO App"}

@app.get('/test')
def test():
    try:
        a=connect()
        return a
    except Exception as e:
        return str(e)

app.include_router(router)
app.include_router(todoapi)
