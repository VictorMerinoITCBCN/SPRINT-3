from fastapi import APIRouter
from services import user_services
from pydantic import BaseModel
from datetime import date

router = APIRouter()

class GetAssistancesParams(BaseModel):
    user_id: int
    date: date

@router.get("/schedule/{user_id}")
def get_schedule(user_id: int):
    return user_services.get_schedule(user_id)

@router.post("/assistances")
def get_assistances(params: GetAssistancesParams):
    return user_services.get_assistances(params.user_id, params.date)