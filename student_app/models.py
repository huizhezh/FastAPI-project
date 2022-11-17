from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum
from .database import Base
from .schemas import Gender


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(500))
    last_name = Column(String(500))
    gender = Column(Enum(Gender))
    date_of_birth = Column(Date)
    major = Column(String(500))


