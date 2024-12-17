from fastapi import APIRouter
from services import user_services
from pydantic import BaseModel
from datetime import date

router = APIRouter()

@router.get("/schedule/{user_id}")
def get_schedule(user_id: int):
    return user_services.get_schedule(user_id)

@router.get("/assistances/{user_id}")
def get_assistances(user_id: int):
    return user_services.get_assistances(user_id)

@router.get("/users")
def get_users():
    return user_services.get_users()

@router.get("/subjects")
def get_subjects():
    return user_services.get_subjects()