from contextlib import asynccontextmanager

from database import create_db_and_tables, SessionLocal
from subject_registry import create_subjects
from config import settings
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    create_subjects()
    yield

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return FileResponse("static/index.html")

from routers.exams import router as exams_router
from routers.users import router as users_router
from routers.auth import router as auth_router
from routers.subjects import router as subjects_router

app.include_router(auth_router)
app.include_router(exams_router)
app.include_router(users_router)
app.include_router(subjects_router)
