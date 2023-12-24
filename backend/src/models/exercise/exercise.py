from sqlalchemy import Column, Integer, String, Boolean

from database.database import Base

class Exercise(Base):
    __tablename__ = 'Exercise'

    id = Column(Integer, primary_key=True, autoincrement=True)
    theme = Column(String, nullable=False)

    