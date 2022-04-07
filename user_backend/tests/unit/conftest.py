import pytest

from user_backend.application import dataclasses


@pytest.fixture
def user():
    return dataclasses.User(
        id=1,
        username='Username',
    )