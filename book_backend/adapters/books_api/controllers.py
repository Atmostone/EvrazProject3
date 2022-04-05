from classic.components import component

from .join_points import join_point
from application import services


@component
class Book:
    book: services.Book

    @join_point
    def on_get_get_books(self, request, response):
        books = self.book.get_books()
        print('Controller!')
        response.media = {
            'books': books,
        }