from __future__ import annotations
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from schemas.filters import GetUserFilter, PatchUserFilter, GetExerciseFilter

from repositories.studentRepositories import StudentRepostitore
from schemas.dtos import SaveUserDto
from models.users.student import Student

class StudentService():
    def __init__(self, db: AsyncSession):
        self._database = StudentRepostitore(db) 

    @staticmethod
    @asynccontextmanager
    async def from_engine(engine: AsyncEngine):
        async with AsyncSession(engine) as session:
            async with session.begin():
                yield StudentService.from_session(session)

    @staticmethod
    def from_session(session: AsyncSession) -> StudentService:
        database = StudentRepostitore(session)
        return StudentService(database)

    async def save_student(self, dto: SaveUserDto):
        model = Student(
            name=dto.name,
            role=dto.role,
            hashed_password=dto.password
        )
        return await self._database.create_student(model)
    
    async def delete_student(self, filter: GetUserFilter):
        return await self._database.delete_student(filter)
    
    async def read_student(self, filter: GetUserFilter):
        return await self._database.read_student(filter)

    async def update_student(self, filter: PatchUserFilter):
        return await self._database.update_student(filter)
    
    async def get_exercise(self, filter: GetExerciseFilter):
        return await self._database.get_random_exercise(filter)
    
    async def get_questions(self, exercise_id: int):
        return await self._database.get_questions(exercise_id)
    
    async def get_answer(self, question_id: int):
        return await self._database.get_answer(question_id)
    
    async def get_right_answer(self, question_id: int):
        return await self._database.get_right_answer(question_id)
    
    async def get_exercise_by_id(self, exercise_id: int):
        return await self._database.get_exercise_by_id(exercise_id)