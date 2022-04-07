from unittest.mock import Mock

import pytest

from classic.messaging import Publisher

from application import interfaces


@pytest.fixture(scope='function')
def users_repo(user):
    users_repo = Mock(interfaces.UsersRepo)
    users_repo.add_user = Mock(return_value=user)
    users_repo.get_user = Mock(return_value=user)
    users_repo.get_users = Mock(return_value=[user])
    users_repo.delete_user = Mock(return_value=None)
    return users_repo


@pytest.fixture(scope='function')
def user_publisher():
    user_publisher = Mock(Publisher)
    user_publisher.plan = Mock(return_value=None)
    return user_publisher
