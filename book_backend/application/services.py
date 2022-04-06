from typing import Optional

from classic.app import DTO
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher
from pydantic import validate_arguments

from application import interfaces, dataclasses

join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    id: Optional[int]
    title: str
    text: str

@component
class Book:
    books_repo: interfaces.BooksRepo
    publisher: Publisher

    @join_point
    @validate_arguments
    def get_books(self):
        books = self.books_repo.get_books()
        if not books:
            raise Exception
        return books

    @join_point
    @validate_arguments
    def add_book(self, title, text):
        book = BookInfo(title=title, text=text).create_obj(dataclasses.Book)
        self.books_repo.add_book(book)

        if self.publisher:
            self.publisher.plan(
                Message('test', {'test': 1})
            )
