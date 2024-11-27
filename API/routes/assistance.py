from fastapi import APIRouter
from services import assistance_services
from pydantic import BaseModel

router = APIRouter()

class Assistance(BaseModel):
    student_id: int
    teacher_id: int
    subject_id: int
    assistance_status: str

@router.get("/assistance/")
def get(user_id, subject_id: int):
    return assistance_services.get_by_student_and_subject(user_id, subject_id)

@router.post("/assistance")
def create(assistance: Assistance):
    return assistance_services.create(assistance)