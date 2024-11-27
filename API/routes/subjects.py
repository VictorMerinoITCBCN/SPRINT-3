from fastapi import APIRouter
from services import subject_services
from pydantic import BaseModel

router = APIRouter()

class Subject(BaseModel):
    name: str
    room: str
    teacher_id: int
    weekday: int
    start_time: str
    end_time: str

@router.get("/subject/{id}")
def get_subject(id: int):
    return subject_services.get(id)

@router.post("/subject")
def create_subject(subject: Subject):
    return subject_services.create(subject)

@router.post("/matriculate")
def matriculate(user_id: int, subject_id: int):
    return subject_services.matriculate(user_id, subject_id)

@router.get("/subject/{id}/users")
def get_users(id: int):
    return subject_services.get_users(id)