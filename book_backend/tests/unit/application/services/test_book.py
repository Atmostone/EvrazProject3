import pytest

from book_backend.application.services import Book


@pytest.fixture(scope='function')
def service(books_repo, book_publisher):
    return Book(
        books_repo=books_repo,
        publisher=book_publisher,
    )


def test__get_book(service, books_repo):
    id = 1
    service.get_book(id=id)
    call_args, _ = books_repo.get_book.call_args
    assert call_args == (id,)


def test__add_book(service, books_repo):
    data = {
        'title': 'Title1',
        'description': 'Desc1',
    }
    assert service.add_book(**data) is None


def test__get_books(service, book):
    assert service.get_books() == [book, ]


def test__delete_book(service, book):
    data = {
        'title': 'Title1',
        'description': 'Desc1',
    }
    service.add_book(**data)

    assert service.delete_book(id=1) is None


def test__take_book(service, book):
    data = {
        'id': 1,
        'user_id': 1,
    }
    assert service.take_book(**data) == book


def test__return_book(service, book):
    data = {
        'id': 1,
    }
    assert service.return_book(**data) == book
