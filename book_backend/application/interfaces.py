from abc import ABC, abstractmethod
from typing import Optional

from application.dataclasses import Book


class BooksRepo(ABC):
    @abstractmethod
    def get_books(self) -> Optional[Book]:
        ...
