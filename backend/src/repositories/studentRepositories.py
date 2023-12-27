import random

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete, select, and_
from fastapi import HTTPException


from models.users.student import Student
from models.exercise.exercise import Exercise
from models.exercise.answer import Answer
from models.exercise.question import Question
from schemas.filters import GetUserFilter, PatchUserFilter, GetExerciseFilter

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
    
    async def get_random_exercise(self, filter: GetExerciseFilter) -> Exercise:
        stmt = select(Exercise).order_by(Exercise.theme, Exercise.level)
        stmt = stmt.where(and_(Exercise.theme == filter.theme, Exercise.level == filter.level))
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Exercise not found")
        return random.choice(items)
    
    async def get_questions(self, exercise_id: int) -> list[Question]:
        stmt = select(Question).where(Question.exercise_id == exercise_id)
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Questions not found")
        return items 
    

    async def get_answer(self, question_id: int) -> list[Answer]:
        stmt = select(Answer).where(Answer.question_id == question_id)
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Answers not found")
        return items 
    
    async def get_right_answer(self, question_id) -> Answer:
        stmt = select(Answer).where(Answer.question_id == question_id)
        stmt = stmt.where(Answer.is_correct == True)
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Right question not found")
        return items[0]

    async def get_exercise_by_id(self, id: int) -> Exercise:
        stmt = select(Exercise).where(Exercise.id == id)
        results = await self.session.scalars(stmt)
        items = list(results.all())
        if not items:
            raise HTTPException(status_code=404, detail="Exercise not found")
        return items[0]
