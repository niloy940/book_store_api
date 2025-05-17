from sqlalchemy.orm import Session
from app.models import Book
from app.schemas import BookCreate, BookUpdate
from typing import Optional
from utils.pagination import paginate
from sqlalchemy import or_

def get_all_books(db: Session, skip=0, limit=10, search: Optional[str] = None):
    query = db.query(Book)

    if search:
        query = query.filter(
            or_(
                Book.title.ilike(f"%{search}%"),
                Book.author.ilike(f"%{search}%")
            )
        )

    return paginate(query, skip, limit)

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, data: BookCreate):
    book = Book(**data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book(db: Session, book_id: int, data: BookUpdate):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True
