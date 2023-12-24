from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete, select
from fastapi import HTTPException


from models.users.teacher import Teacher
from schemas.filters import GetUserFilter, PatchUserFilter

class FileObjectRepostitore:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def create_teacher(self, model: Teacher):
        async with self.session.begin_nested():
            self.session.add(model)
            await self.session.flush()

        return model


    async def delete_teacher(self, filter: GetUserFilter):
        models = await self.read_teacher(filter)
        for model in models:
            await self.session.delete(model)
        #await self.session.commit()
        return {'ok': True}
    
    

    async def read_teacher(self, filter: GetUserFilter) -> list[Teacher]:
        stmt = select(Teacher).order_by(Teacher.id, Teacher.name)
        if filter.id is not None:
            stmt = stmt.where(Teacher.id == filter.id)
        if filter.name is not None:
            stmt = stmt.where(Teacher.name.ilike(filter.name))
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return items 
    
    
    async def update_file(self, filter: PatchUserFilter):
        teacher = await self.read_teacher(filter)
        if filter.name is not None:
            teacher.name = filter.name
        if filter.path is not None:
            teacher.password = filter.password
        return await self.create_teacher(teacher)

    
        


