from sqlalchemy.orm import Session
from app.models import Book
from app.schemas import BookCreate, BookUpdate

def get_all_books(db: Session, skip=0, limit=10):
    return db.query(Book).offset(skip).limit(limit).all()

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
    for key, value in data.dict(exclude_unset=True).items():
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
