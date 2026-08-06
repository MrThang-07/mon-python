from database import engine, get_db
from fastapi import Depends, FastAPI, status
from models import Base, BookModel
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management API - MySQL & SQLAlchemy", version="1.0.0")


class BookCreate(BaseModel):
    code: str
    title: str
    price: float
    pages: int


class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True


@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookModel(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get("/books", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()