#path parameters
from fastapi import FastAPI
app=FastAPI()
@app.get("/T2")
async def TestCase1(name:str):
    return {"name":name}

