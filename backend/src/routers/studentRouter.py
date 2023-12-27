import os

from typing import Annotated, Any, AsyncGenerator, Callable, Optional

from fastapi import APIRouter, Depends, Form, HTTPException, Query, Request, status
from pydantic import BaseModel

from schemas.filters import GetUserFilter, PatchUserFilter, GetExerciseFilter
from services.studentService import StudentService
from schemas.dtos import SaveUserDto
from routers.authRouter import hash_password
from shared.shared import ExerciseLevel, ExerciseTopic



SECRET_KEY = os.environ["SECRET_AUTH"]
ALGORITHM = os.environ["AUTH_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["AUTH_ACCESS_TOKEN_EXPIRE_MINUTES"])

class TokenData(BaseModel):
    username: str | None = None

def create_router(
    get_service: Callable[[], AsyncGenerator[StudentService, Any]],
) -> APIRouter:
    router = APIRouter()

    @router.post(
        "/student/{name}/{password}/",
        name="Add student",
    )
    async def add_student(
        name: str, 
        password: str,
        service: StudentService = Depends(get_service),
    ):
        dto = SaveUserDto(
            name=name,
            role='Student',
            password=hash_password(password)
        )
        return await service.save_student(dto)
    
    @router.delete(
        "/student/{id}/",
        name="Delete student",
    )
    async def delete_student(
        id: int,
        name: Optional[str] = None,
        service: StudentService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.delete_student(filter)
    
    @router.get(
        "/student/{id}/",
        name="Get student",
    )
    async def read_student(
        id: int,
        name: Optional[str] = None,
        service: StudentService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.read_student(filter)


    @router.patch(
        "/student/{id}/",
        name="Patch student",
    )
    async def update_student(
        id: int, 
        name: Optional[str] = None,
        password: Optional[str] = None,
        service: StudentService = Depends(get_service),
    ):
        filter = PatchUserFilter(       
            id=id, 
            name=name,
            password=hash_password(password)
        )
        return await service.update_student(filter)
    

    @router.get(
        "/exercise/{theme}/{level}/",
        name="Get random exercise",
    )
    async def get_random_exercise(
        theme: str,
        level: str,
        service: StudentService = Depends(get_service),
    ):
        filter = GetExerciseFilter(
            theme=get_exercise_theme_enum(theme),
            level=get_exercise_level_enum(level)
        )
        return await service.get_exercise(filter)
    

    @router.get(
        "/exercise/{id}/",
        name="Get exercise",
    )
    async def get_exercise_by_id(
        id: int, 
        service: StudentService = Depends(get_service),
    ):
        return await service.get_exercise_by_id(id)

    
    @router.get(
        "/exercise/question/{question_id}/answers/",
        name="Get question answers",
    )
    async def get_answers(
        question_id: int,
        service: StudentService = Depends(get_service),
    ):
        return await service.get_answer(question_id)
    
    @router.get(
        "/exercise/question/{question_id}/right-answer/",
        name="Get right answer for question",
    )
    async def get_right_answer(
        question_id: int,
        service: StudentService = Depends(get_service),
    ):
        return await service.get_right_answer(question_id)
    
    @router.get(
        "/{exercise_id}/questions/",
        name="Get questions for exercise",
    )
    async def get_questions(
        exercise_id: int,
        service: StudentService = Depends(get_service),
    ):
        return await service.get_questions(exercise_id)
    
    
    return router


def get_exercise_theme_enum(exercise_topic: str):
    if exercise_topic == "Math":
        return ExerciseTopic.MATH
    elif exercise_topic == "English":
        return ExerciseTopic.ENGLISH
    elif exercise_topic == "Nature":
        return ExerciseTopic.NATURE
    else:
        return None
    
def get_exercise_level_enum(exercise_level: str):
    if exercise_level == "Easy":
        return ExerciseLevel.EASY
    elif exercise_level == "Medium":
        return ExerciseLevel.MEDIUM
    elif exercise_level == "Hard":
        return ExerciseLevel.HARD
    else: return None