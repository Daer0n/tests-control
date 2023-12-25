from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    role: str
    password: str

class UserRead(BaseModel):
    id: int 
    name: str
    role: str
    password: str