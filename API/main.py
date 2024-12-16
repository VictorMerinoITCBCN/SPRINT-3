from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import session, user, teacher, admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)

app.include_router(session.router)
app.include_router(user.router)
app.include_router(teacher.router)
app.include_router(admin.router)