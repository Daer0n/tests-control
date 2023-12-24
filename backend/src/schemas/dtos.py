from pydantic import BaseModel

class SaveUserDto(BaseModel):
    name: str
    role: str
    password: str