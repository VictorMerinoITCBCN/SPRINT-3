from fastapi import APIRouter
from pydantic import BaseModel
from services import admin_services

router = APIRouter()

class User(BaseModel):
    name: str
    last_name: str
    email: str
    group_id: int

@router.post("/register/student")
def register_student(user: User):
    return admin_services.register_user(user, 1)