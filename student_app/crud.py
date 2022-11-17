from sqlalchemy.orm import Session

from . import models, schemas


def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_student_by_firstname(db: Session, student_first_name: str):
    return db.query(models.Student).filter(models.Student.first_name == student_first_name).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    # db_student = models.Student(first_name = student.first_name, last_name = student.last_name,
    #                             gender = student.gender, date_of_birth = student.date_of_birth, major = student.major )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
