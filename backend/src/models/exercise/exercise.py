from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.types import Enum as EnumType

from database.database import Base
from shared.shared import ExerciseLevel, ExerciseTopic

class Exercise(Base):
    __tablename__ = 'Exercise'

    id = Column(Integer, primary_key=True, autoincrement=True)
    theory = Column(String, nullable=False)
    theme = Column(EnumType(ExerciseTopic, create_constraint=False), nullable=False)
    level = Column(EnumType(ExerciseLevel, create_constraint=False), nullable=False)