from fastapi import APIRouter
from pydantic import BaseModel
import services.users_services as users_services

router = APIRouter()

class User(BaseModel):
    name: str
    last_name: str
    email: str
    group_id: int
    role_id: int

@router.get("/user/{id}")
def get_user(id: int):
    return users_services.get(id)

@router.post("/user")
def create_user(user: User):
    return users_services.create(user)