import os

from typing import Annotated, Any, AsyncGenerator, Callable, Optional

from fastapi import APIRouter, Depends, Form, HTTPException, Query, Request, status
from pydantic import BaseModel

from schemas.filters import GetUserFilter, PatchUserFilter
from services.teacherService import TeacherService
from schemas.schemas import UserCreate
from schemas.dtos import SaveAnswerDto, SaveUserDto, SaveQuestionDto, SaveExerciseDto
from routers.authRouter import hash_password

from shared.shared import ExerciseLevel
from shared.shared import ExerciseTopic




SECRET_KEY = os.environ["SECRET_AUTH"]
ALGORITHM = os.environ["AUTH_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["AUTH_ACCESS_TOKEN_EXPIRE_MINUTES"])

class TokenData(BaseModel):
    username: str | None = None

def create_router(
    get_service: Callable[[], AsyncGenerator[TeacherService, Any]],
) -> APIRouter:
    router = APIRouter()

    @router.post(
        "/teacher/{name}/{password}/",
        name="Add teacher",
    )
    async def add_teacher(
        name: str, 
        password: str,
        service: TeacherService = Depends(get_service),
    ):
        dto = SaveUserDto(
            name=name,
            role='Teacher',
            password=hash_password(password)
        )
        return await service.save_teacher(dto)
    
    @router.delete(
        "/teacher/{id}/",
        name="Delete teacher",
    )
    async def delete_teacher(
        id: int,
        name: Optional[str] = None,
        service: TeacherService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.delete_teacher(filter)
    
    @router.get(
        "/teacher/{id}/",
        name="Get teacher",
    )
    async def read_teacher(
        id: int,
        name: Optional[str] = None,
        service: TeacherService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.read_teacher(filter)


    @router.patch(
        "/teacher/{id}/",
        name="Patch teacher",
    )
    async def update_teacher(
        id: int, 
        name: Optional[str] = None,
        password: Optional[str] = None,
        service: TeacherService = Depends(get_service),
    ):
        filter = PatchUserFilter(       
            id=id, 
            name=name,
            password=hash_password(password)
        )
        return await service.update_teacher(filter)
    
    @router.post(
        "/exercise/{theory}/{theme}/{level}/",
        name="Add exercise",
    )
    async def add_exercise(
        theory: str,
        theme: ExerciseTopic,
        level: ExerciseLevel, 
        service: TeacherService = Depends(get_service),
    ):
        dto = SaveExerciseDto(
            theory=theory,
            theme=theme,
            level=level
        )
        return await service.save_exercise(dto)
    
    @router.post(
        "/question/{question_text}/{exercise_id}/",
        name="Add question",
    )
    async def add_question(
        question_text: str,
        exercise_id: int,
        service: TeacherService = Depends(get_service),
    ):
        dto = SaveQuestionDto(
            question_text=question_text,
            exercise_id=exercise_id
        )
        print(dto.question_text, dto.exercise_id)
        return await service.save_question(dto)
    
    @router.post(
        "/answer/{text}/{is_correct}/{question_id}/",
        name="Add answer",
    )
    async def add_answer(
        text: str,
        is_correct: bool,
        question_id: int,
        service: TeacherService = Depends(get_service),
    ):
        dto = SaveAnswerDto(
            text=text,
            is_correct=is_correct,
            question_id=question_id
        )
        return await service.save_answer(dto)


    return router
