from abc import ABC, abstractmethod
from typing import Optional

from application.dataclasses import Book


class BooksRepo(ABC):
    @abstractmethod
    def get_books(self) -> Optional[Book]:
        ...

    @abstractmethod
    def get_book(self, id) -> Optional[Book]:
        ...

    @abstractmethod
    def add_book(self, book):
        ...

    @abstractmethod
    def delete_book(self, id):
        ...

