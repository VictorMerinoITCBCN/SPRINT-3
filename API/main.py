from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import users, groups, subjects, assistance

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por el origen específico de tu front-end para mayor seguridad.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(groups.router)
app.include_router(subjects.router)
app.include_router(assistance.router)