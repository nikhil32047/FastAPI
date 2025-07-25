from fastapi import FastAPI
app=FastAPI()
@app.get("/T1")
async def TestCase1():
    return {"Data":"Welcome to FastAPI Development for AI/ML applications"}
