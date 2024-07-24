from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return ("This is basic FastAPI application.")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}