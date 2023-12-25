from __future__ import annotations
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from schemas.filters import GetUserFilter, PatchUserFilter

from repositories.teacherRepositories import TeacherRepostitore
from schemas.dtos import SaveUserDto
from models.users.teacher import Teacher

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