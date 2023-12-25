from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

from database.database import engine
from services.studentService import StudentService
from routers.studentRouter import create_router as create_user_touter


app = FastAPI(
    title="Tests portal"
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PATCH"],
    allow_headers=["*"],
)

SessionLocal = async_sessionmaker(expire_on_commit=False, bind=engine)

async def get_student_service():
    async with SessionLocal() as session:
        async with session.begin():
            service = StudentService(session)
            yield service

student_router = create_user_touter(get_student_service)
app.include_router(student_router, prefix="/student", tags=["student"])