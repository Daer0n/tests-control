from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from database.database import Base
from models.exercise.question import Question

class Answer(Base):
    __tablename__ = 'Answer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(Integer, ForeignKey(Question.id))
