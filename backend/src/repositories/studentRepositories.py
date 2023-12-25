from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete, select
from fastapi import HTTPException


from models.users.student import Student
from schemas.filters import GetUserFilter, PatchUserFilter

class StudentRepostitore:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def create_student(self, model: Student):
        async with self.session.begin_nested():
            self.session.add(model)
            await self.session.flush()
        return model


    async def delete_student(self, filter: GetUserFilter):
        models = await self.read_student(filter)
        for model in models:
            await self.session.delete(model)
        return {'ok': True}
    
    

    async def read_student(self, filter: GetUserFilter) -> list[Student]:
        stmt = select(Student).order_by(Student.id, Student.name)
        if filter.id is not None:
            stmt = stmt.where(Student.id == filter.id)
        if filter.name is not None:
            stmt = stmt.where(Student.name.ilike(filter.name))
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Student not found")
        return items 
    
    
    async def update_student(self, filter: PatchUserFilter):
        user_filter = GetUserFilter(
            id=filter.id,
            name=filter.name
        )
        student = await self.read_student(user_filter)
        if filter.name is not None:
            student.name = filter.name
        if filter.password is not None:
            student.password = filter.password
        return await self.create_student(student)

    
        


