from fastapi import APIRouter
from services import teacher_services, session_services
from pydantic import BaseModel

router = APIRouter()

class Assistance(BaseModel):
    student_id: int
    subject_id: int
    assistance_status: str

#Get all assistances
@router.get("/assistance/subject/{subject_id}")
def read_assistances(subject_id: int, token: str):
    is_valid_user = session_services.validate_role(token, [2, 3])
    if not is_valid_user["ok"]: return is_valid_user

    return teacher_services.read_assistances(subject_id)

#Matriculate student in a subject
@router.get("/matriculate")
def matriculate(user_id: int, subject_id: int, token: str):
    is_valid_user = session_services.validate_role(token, [2, 3])
    if not is_valid_user["ok"]: return is_valid_user

    return teacher_services.matriculate(user_id, subject_id)

#Get the teacher subjects
@router.get("/subjects/{teacher_id}")
def get_teacher_subjects(teacher_id: int, token: str):
    is_valid_user = session_services.validate_role(token, [2, 3])
    if not is_valid_user["ok"]: return is_valid_user

    return teacher_services.get_subjects(teacher_id)

#Modify assistance
@router.put("/assistance/{id}")
def modify_assistance(assistance: Assistance, token: str, id: int = None):
    is_valid_user = session_services.validate_role(token, [2, 3])
    if not is_valid_user["ok"]: return is_valid_user

    if id: return teacher_services.modify_assistance(id, assistance)
    return teacher_services.create_assistance(assistance)