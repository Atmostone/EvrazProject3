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

    @join_point
    def on_get_info(self, request, response):
        book = self.book.get_book(
            **request.media,
        )
        response.media = {
            'book': str(book),
        }

    @join_point
    def on_post_take_book(self, request, response):
        self.book.take_book(
            **request.media,
        )
        response.media = {
            'message': 'Книга взята'
        }

    @join_point
    def on_post_return_book(self, request, response):
        self.book.return_book(
            **request.media,
        )
        response.media = {
            'message': 'Книга возвращена'
        }
