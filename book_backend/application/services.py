from datetime import datetime
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
    description: str
    user_id: Optional[int]


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
    def add_book(self, title, description):
        book = BookInfo(title=title, description=description).create_obj(dataclasses.Book)
        self.books_repo.add_book(book)

        if self.publisher:
            self.publisher.plan(
                Message('test', {'event': 'add_book', 'created': datetime.now(),
                                 'book_id': book.id, 'user_id': None})
            )
