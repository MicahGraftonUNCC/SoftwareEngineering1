# add all code from part one of assignment 4
from typing import Union

from fastapi import FastAPI

app = FastAPI()
#commit comment
#Method 1, part 1
@app.get("/")
def read_root():
    return {"Hello": "World"}

#Method 2, part1
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
