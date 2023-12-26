from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from database.database import Base
from models.exercise.exercise import Exercise

class Question(Base):
    __tablename__ = 'Question'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String, nullable=False)
    exercise_id = Column(Integer, ForeignKey(Exercise.id))

    