from typing import Optional
from pydantic import BaseModel

class ItemIn(BaseModel):
  name: str
  price: float
  is_offer: Optional[bool] = None

class ItemOut(ItemIn):
  id: int

class ItemInDB(ItemIn):
  password: str