from typing import Optional, List
from pydantic import BaseModel

items = {}

class ItemBase(BaseModel):
  name: str
  price: float
  is_offer: Optional[bool] = None

class ItemOut(ItemBase):
  id: int
  @staticmethod
  def all():
    return [ItemOut(id=id, **d.dict()) for (id, d) in items.items()]
  @staticmethod
  def get(id: int):
    return id in items and ItemOut(id=id, **items[id].dict()) or None
  @staticmethod
  def delete(id: int):
    del items[id]
  @staticmethod
  def update(id: int, d:dict):
    items[id].update(d)

class ItemIn(BaseModel):
  def save(self) -> ItemOut:
    id = len(items) + 1
    items[id] = ItemIn(**self.dict())