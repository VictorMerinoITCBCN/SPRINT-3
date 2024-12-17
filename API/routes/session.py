from fastapi import APIRouter
from pydantic import BaseModel
from passlib.context import CryptContext
from services import session_services


class User(BaseModel):
    name: str
    last_name: str
    email: str
    group_id: int
    password: str

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    token: str

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_pwd: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(plain_pwd, hashed_pwd)

@router.post("/register/{role_id}")
def register(role_id: int, user: User):
    # is_valid_user = session_services.validate_role(token, [2, 3])
    # if not is_valid_user["ok"]: return is_valid_user

    user.password = hash_password(user.password)
    return session_services.register(role_id, user)

@router.post("/login")
def login(login: Login):
    return session_services.login(login.email, login.password, pwd_context)

@router.post("/user")
def get_user(token: Token):
    return session_services.get_user(token.token)