from sqlalchemy import Column, Integer, String, Boolean
from models.users.user import User

from database.database import Base

class Student(User):
    __tablename__ = 'Student'

    role = Column(String, default='Teacher')
