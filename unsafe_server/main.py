from typing import Optional
from fastapi import FastAPI

from .models.item import ItemIn, ItemOut

app = FastAPI()

@app.post("/items/")
def post_item(item: ItemIn):
    return {
        "name": item.name,
        "price": item.price
    }

@app.get("/items/{item_id}", response_model=ItemOut)
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "id": item_id,
        "name": q,
        "price": 0.0
        }
