from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_student_by_firstname(db: Session, full_name: str):
    return db.query(models.Student).filter(models.Student.first_name + models.Student.last_name == full_name).first()


@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentBase, db: Session = Depends(get_db)):
    full_name = student.first_name + student.last_name
    db_student = get_student_by_firstname(db, full_name=full_name)
    if db_student:
        raise HTTPException(status_code=400, detail="Name already registered")
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students/", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Student).offset(skip).limit(limit).all()


@app.get("/students/id/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.get("/students/firstname/{student_firstname}", response_model=schemas.Student)
def read_student(student_firstname: str, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.first_name == student_firstname).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
