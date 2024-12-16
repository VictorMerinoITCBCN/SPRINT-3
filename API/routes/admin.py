from fastapi import APIRouter
from pydantic import BaseModel
from datetime import time
from services import admin_services

router = APIRouter()

class Subject(BaseModel):
    name: str
    room: str
    teacher_id: int
    weekday: int
    start_time: time
    end_time: time

@router.post("/subject")
def create_subject(subject: Subject):
    return admin_services.create_subject(subject)