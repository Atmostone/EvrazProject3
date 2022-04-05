from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select

from application.interfaces import BooksRepo
from application.dataclasses import Book


@component
class BooksRepo(BaseRepository, BooksRepo):
    def get_books(self) -> Optional[Book]:
        query = select(Book)
        return self.session.execute(query).scalars().all()

    def add_book(self, book):
        self.session.add(book)
        self.session.flush()
        return book.id
