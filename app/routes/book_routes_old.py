from fastapi import APIRouter, HTTPException
from app.schemas import BookCreate, BookRead, BookUpdate
from app.crud import get_all_books, get_book_by_id, create_book, update_book, delete_book

router = APIRouter()

@router.get("/", response_model=list[BookRead])
def list_books():
    return get_all_books()

@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int):
    book = get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookRead)
def add_book(book_data: BookCreate):
    return create_book(book_data)

@router.put("/{book_id}", response_model=BookRead)
@router.patch("/{book_id}", response_model=BookRead)
def update(book_id: int, book_data: BookUpdate):
    updated = update_book(book_id, book_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}")
def delete(book_id: int):
    deleted = delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": f"Book {book_id} deleted"}
