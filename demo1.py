#Simple FastAPI application
from fastapi import FastAPI
app=FastAPI()
@app.get("/T1")
async def TestCase1():
    return {"Data":"Welcome to FastAPI Development for AI/ML application"}


#path parameters
from fastapi import FastAPI
app=FastAPI()
@app.get("/T2")
async def TestCase1(name:str):
    return {"name":name}



#query parameters(combination of path parameter)
from fastapi import FastAPI
app=FastAPI()
@app.get("/T3")
async def TestCase1(number:int,name:str):
    return {"number":number,"name":name}




