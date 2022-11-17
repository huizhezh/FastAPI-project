import datetime
from datetime import date
from enum import Enum
from typing import Union, List, Optional

from pydantic import BaseModel

class Gender(str, Enum):
    female = 'F'
    male = 'M'


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    date_of_birth: Union[date, None] = None
    major: Optional[str] = None
    class Config:
        orm_mode = True

class Student(StudentBase):
    id: int





