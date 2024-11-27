from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import teacher, admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teacher.router)
app.include_router(admin.router)