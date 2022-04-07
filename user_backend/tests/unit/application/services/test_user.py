import pytest

from application.services import User


@pytest.fixture(scope='function')
def service(users_repo, user_publisher):
    return User(
        users_repo=users_repo,
        publisher=user_publisher,
    )


def test__get_user(service, users_repo):
    id = 1
    service.get_user(id=id)
    call_args, _ = users_repo.get_user.call_args
    assert call_args == (id,)


def test__add_user(service, users_repo):
    data = {
        'username': 'User',
    }
    assert service.add_user(**data) is None


def test__get_users(service, user):
    assert service.get_users() == [user, ]


def test__delete_user(service, user):
    data = {
        'username': 'User',
    }
    service.add_user(**data)

    assert service.delete_user(id=1) is None
