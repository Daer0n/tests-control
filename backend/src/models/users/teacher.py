from sqlalchemy import Column, Integer, String, Boolean
from models.users.user import User

from database.database import Base

class Teacher(User):
    __tablename__ = 'Teacher'

    role = Column(String, default='Teacher')
