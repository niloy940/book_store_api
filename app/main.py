from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router as book_router
from app.models import Book

Base.metadata.create_all(bind=engine)

app = FastAPI()

#register routes
app.include_router(book_router, prefix="/books", tags=["Books"])

@app.get("/")
def root():
    return {"Welcome to Bookstore API"}