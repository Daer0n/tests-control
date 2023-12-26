from __future__ import annotations
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from schemas.filters import GetUserFilter, PatchUserFilter

from repositories.teacherRepositories import TeacherRepostitore
from schemas.dtos import SaveUserDto, SaveAnswerDto, SaveExerciseDto, SaveQuestionDto
from models.users.teacher import Teacher
from models.exercise.exercise import Exercise
from models.exercise.answer import Answer
from models.exercise.question import Question

class TeacherService():
    def __init__(self, db: AsyncSession):
        self._database = TeacherRepostitore(db) 

    @staticmethod
    @asynccontextmanager
    async def from_engine(engine: AsyncEngine):
        async with AsyncSession(engine) as session:
            async with session.begin():
                yield TeacherService.from_session(session)

    @staticmethod
    def from_session(session: AsyncSession) -> TeacherService:
        database = TeacherRepostitore(session)
        return TeacherService(database)

    async def save_teacher(self, dto: SaveUserDto):
        model = Teacher(
            name=dto.name,
            role=dto.role,
            hashed_password=dto.password
        )
        return await self._database.create_teacher(model)
    
    async def delete_teacher(self, filter: GetUserFilter):
        return await self._database.delete_teacher(filter)
    
    async def read_teacher(self, filter: GetUserFilter):
        return await self._database.read_teacher(filter)

    async def update_teacher(self, filter: PatchUserFilter):
        return await self._database.update_teacher(filter)
    
    async def save_exercise(self, dto: SaveExerciseDto):
        model = Exercise(
            theory=dto.theory,
            theme=dto.theme,
            level=dto.level
        )
        return await self._database.create_exercise(model)
    
    async def save_question(self, dto: SaveQuestionDto):
        model = Question(
            question_text=dto.question_text,
            exercise_id=dto.exercise_id
        )
        return await self._database.create_question(model)
    
    async def save_answer(self, dto: SaveAnswerDto):
        model = Answer(
            text=dto.text,
            is_correct=dto.is_correct,
            question_id=dto.question_id
        )
        return await self._database.create_answer(model)
