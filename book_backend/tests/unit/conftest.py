import pytest

from book_backend.application import dataclasses


@pytest.fixture
def book():
    return dataclasses.Book(
        id=1,
        title='Title',
        description='Desc',
    )