from sqlalchemy import Column, Integer, String, Boolean


from database.database import Base

class User(Base):
    __tablename__ = 'User'
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    