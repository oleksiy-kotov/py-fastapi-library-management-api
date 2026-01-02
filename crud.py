from sqlalchemy.orm import Session

import models
import schemas


def get_all_authors(db: Session):
    return db.query(models.DBAuthor).all()

def get_author_by_name(db: Session, name: str):
    return db.query(models.DBAuthor).filter(models.DBAuthor.name == name).first()

def get_author_by_id(db: Session, id: int):
    return db.query(models.DBAuthor).filter(models.DBAuthor.id == id).first()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.DBAuthor(
        name=author.name,
        bio=author.bio,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_all_books(db: Session,
                  title: str | None = None,
                  author: str | None = None):
    queryset = db.query(models.DBBook)

    if title is not None:
        queryset = queryset.filter(models.DBBook.title == title)
    if author is not None:
        queryset = queryset.filter(models.DBAuthor.id == author)
    return queryset.all()

def get_book_by_id(db: Session, id: int):
    return db.query(models.DBBook).filter(models.DBBook.id == id).first()

def get_book_by_title(db: Session, title: str):
    return db.query(models.DBBook).filter(models.DBBook.title == title).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.DBBook(
        title=book.title,
        author_id=book.authors_id,
        summary=book.summary,
        publication_date=book.publication_date,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book