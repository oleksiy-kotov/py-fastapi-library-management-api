from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict


class Author(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    bio: str

class AuthorCreate(Author):
    pass

class Book(BaseModel):
    id: int
    title: str
    summary: str
    publication_date: date
    author: Author
    model_config = ConfigDict(from_attributes=True)

class BookCreate(BaseModel):
    title: str
    summary: str
    author_id: int
    publication_date: date

