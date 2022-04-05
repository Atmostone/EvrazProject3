from classic.components import component

from .join_points import join_point
from application import services


@component
class Book:
    book: services.Book

    @join_point
    def on_get_books(self, request, response):
        books = self.book.get_books()
        response.media = {
            'books': str(books),
        }

    @join_point
    def on_post_add_book(self, request, response):
        self.book.add_book(
            **request.media,
        )
        response.media = {
            'message': 'Книга была создана'
        }
