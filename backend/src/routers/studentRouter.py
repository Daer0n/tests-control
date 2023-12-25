import os

from typing import Annotated, Any, AsyncGenerator, Callable, Optional

from fastapi import APIRouter, Depends, Form, HTTPException, Query, Request, status
from pydantic import BaseModel

from schemas.filters import GetUserFilter, PatchUserFilter
from services.studentService import StudentService
from schemas.schemas import UserCreate
from routers.authRouter import hash_password



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
        dto = UserCreate(
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
    
    return router
