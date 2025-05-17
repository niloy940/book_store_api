from app.models import Book
from app.schemas import BookCreate, BookUpdate
from typing import List, Optional

books: List[Book] = []

def get_all_books() -> List[Book]:
    return books

def get_book_by_id(book_id: int) -> Optional[Book]:
    return next((book for book in books if book.id == book_id), None)

def create_book(data: BookCreate) -> Book:
    new_id = books[-1].id + 1 if books else 1
    new_book = Book(id=new_id, **data.model_dump())
    books.append(new_book)
    return new_book

def update_book(book_id: int, data: BookUpdate)-> Optional[Book]:
    for index, book in enumerate(books):
        if book.id == book_id:
            book_data = books[index].model_dump()
            updated_data = data.model_dump(exclude_unset=True)
            book_data.update(updated_data)
            books[index] = Book(**book_data)
            return books[index]
    return None
    
def delete_book(book_id: int)-> bool:
    for index, book in books:
        if book.id == book_id:
            del books[index]
            return True
    return False