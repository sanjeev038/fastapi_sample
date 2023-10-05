#main.py
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
        return {"message" : "Hellow World"}
    
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}