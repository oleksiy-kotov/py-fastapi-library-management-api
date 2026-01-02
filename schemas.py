from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict


class Author(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    bio: str

class AuthorCreate(Author):
    pass

class Book(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str

class BookCreate(Book):
    title: str
    summary: str
    authors_id: int
    publication_date: date

