from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.book_schema import BookCreate, BookRead, BookUpdate
from app.crud.book_crud import *
from app.dependencies import get_db

router = APIRouter()

@router.get("/")
def list_books(
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return get_all_books(db, skip, limit, search)

@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookRead)
def add_book(book_data: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book_data)

@router.put("/{book_id}", response_model=BookRead)
@router.patch("/{book_id}", response_model=BookRead)
def update(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    book = update_book(db, book_id, book_data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}")
def delete(book_id: int, db: Session = Depends(get_db)):
    deleted = delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": f"Book {book_id} deleted"}
