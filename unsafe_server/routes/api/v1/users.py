from typing import List
from fastapi import APIRouter, HTTPException

from ....models.user import UserLogin, UserOut

router = APIRouter(prefix="/users", tags=["api.v1.users"])

@router.get("/", response_model=List[UserOut])
def get_users():
  return UserOut.all()

@router.post("/", response_model=UserOut)
def create_item(user: UserLogin):
  return user.save()

@router.get("/{user_id}/", response_model=UserOut)
def get_an_user(user_id: int):
  if u := UserOut.get(user_id):
    return u
  else: raise HTTPException(
    status_code=404,
    detail="User not found"
  )

@router.delete("/{user_id}/", response_model=UserOut)
def delete_user(user_id: int):
  if u := UserOut.get(user_id):
    UserOut.delete(user_id)
    return u
  else: raise HTTPException(
    status_code=404,
    detail="User not found"
  )