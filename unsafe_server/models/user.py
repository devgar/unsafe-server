from typing import List
from hashlib import sha256
from pydantic import BaseModel, Field, EmailStr

users = {}

def maxId():
  return max([0, *[k for k in users]])

class UserBase(BaseModel):
  email: EmailStr

class UserDB(UserBase):
  password_256: str

class UserLogin(UserBase):
  password: str = Field(min_length=6, max_length=16)
  def encrypt(self) -> UserDB:
    epass = sha256(bytes(self.password, "utf-8")).hexdigest()
    return UserDB(email=self.email, password_256=epass)
  def save(self) -> "UserOut":
    id = maxId() + 1
    users[id] = self.encrypt()
    return UserOut(id=id, **users[id].dict())

class UserOut(UserBase):
  id: int
  @staticmethod
  def all() -> List["UserOut"]:
    return [UserOut(id=id, **d.dict()) for (id, d) in users.items()]
  @staticmethod
  def get(id: int) -> "UserOut":
    return id in users and UserOut(id = id, **users[id].dict()) or None
  @staticmethod
  def delete(id: int):
    del users[id]
  @staticmethod
  def update(id: int, d: dict):
    users[id].update(d)
