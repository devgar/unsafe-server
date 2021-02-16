from typing import List
from fastapi import APIRouter

from ....models.item import ItemIn, ItemOut

from random import randint

router = APIRouter(prefix = "/items", tags=["api.v1.items"])

@router.get("/", response_model=List[ItemOut])
def get_items():
  return []

@router.post("/")
def create_item(item: ItemIn):
  return {
    "id": randint(1, 999), 
    **item.dict()
  }

@router.get("/{item_id}/", response_model=ItemOut)
def get_an_item(item_id: int):
  return {
    "id": item_id,
    "name": f"Unnamed #{item_id}",
    "price": item_id / 10
  }
