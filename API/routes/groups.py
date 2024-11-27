from fastapi import APIRouter
from pydantic import BaseModel
from services import group_services

class Group(BaseModel):
    name: str

router = APIRouter()

@router.get("/group/{id}")
def get_group(id: int):
    return group_services.get(id)

@router.post("/group")
def create_group(group: Group):
    return group_services.create(group)