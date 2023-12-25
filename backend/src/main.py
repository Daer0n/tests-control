from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

from database.database import engine
from services.studentService import StudentService
from services.teacherService import TeacherService
from routers.studentRouter import create_router as create_student_touter
from routers.teacherRouter import create_router as create_teacher_router
from routers.authRouter import create_router as create_auth_router


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

async def get_teacher_service():
    async with SessionLocal() as session:
        async with session.begin():
            service = TeacherService(session)
            yield service

auth_router = create_auth_router(get_teacher_service, get_student_service)
app.include_router(auth_router, prefix="/auth", tags=["auth"])

student_router = create_student_touter(get_student_service)
app.include_router(student_router, prefix="/student", tags=["student"])

teacher_router = create_teacher_router(get_teacher_service)
app.include_router(teacher_router, prefix="/teacher", tags=["teacher"])