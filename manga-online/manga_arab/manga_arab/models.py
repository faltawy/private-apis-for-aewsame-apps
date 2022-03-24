from datetime import datetime
from lib2to3.pgen2.token import BACKQUOTE
from typing import List,Optional
from pydantic import BaseModel


class Artist(BaseModel):
    id: int
    name: str


class Chapter(BaseModel):
    id: int
    slug: str
    name: str
    number: str
    volume: int
    manga_id: int


class Category(BaseModel):
    id: int
    name: str
    slug: str


class Status(BaseModel):
    id: int
    label: str


class AnimeManga(BaseModel):
    id: int
    name: str
    slug: str
    status_id: int
    other_names: Optional[str]
    summary: str
    cover: str
    caution: int
    views: int
    type_id: int = None
    authors: List[Artist]
    artists:Optional[List[Artist]] 
    status: Optional[Status]
    type: Optional[Status]
    categories: List[Category]
    chapters:Optional[List[Chapter]]




class Category(BaseModel):
    id: int
    name: str
    slug: str
