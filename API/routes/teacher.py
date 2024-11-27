from fastapi import APIRouter
from services import teacher_services
from pydantic import BaseModel

router = APIRouter()

class Assistance(BaseModel):
    student_id: int
    teacher_id: int
    subject_id: int
    assistance_status: str

#Get all assistances
@router.get("/subject/{id}/assistance")
def read_assistances(subject_id: int):
    return teacher_services.read_assistances(subject_id)

@router.get("/matriculate")
def matriculate(user_id: int, subject_id: int):
    return teacher_services.matriculate(user_id, subject_id)

#Modify assistance
@router.put("/subject/assistance/{id}")
def modify_assistance(assistance: Assistance, id: int = None):
    if id: return teacher_services.modify_assistance(id, assistance)
    return teacher_services.create_assistance(assistance)