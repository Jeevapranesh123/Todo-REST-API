from fastapi import FastAPI
from pydantic import BaseModel
from APIs.Auth import router
from APIs.TODO import todoapi


app=FastAPI()


@app.get('/')
def home():
    return {"Details":"REST API's for a TODO App"}


app.include_router(router)
app.include_router(todoapi)