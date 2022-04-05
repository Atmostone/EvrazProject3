from typing import Optional

from classic.app import DTO
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from application import interfaces

join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    id: Optional[int]
    title: str
    text: str

@component
class Book:
    books_repo: interfaces.BooksRepo

    @join_point
    @validate_arguments
    def get_all(self):
        print('Service!')
        books = self.books_repo.get_books()
        if not books:
            raise Exception
        return books


