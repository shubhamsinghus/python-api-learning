from fastapi  import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()
# @app.get("/")
# def root():
#  return {"Mesage":"Bum Bum Bhole"}
# @app.get("/hello")
# def hello():
#     return "Hello World"

class Message(BaseModel):
    message: str

@app.get("/", response_model=Message)
def root():
    return {"mantra": "Bum Bum Bhole"}







