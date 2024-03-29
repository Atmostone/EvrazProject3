from datetime import datetime
from typing import Optional

from classic.app import DTO
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher
from pydantic import validate_arguments

from application import interfaces, dataclasses
from application.exceptions import DoesNotExists

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    id: Optional[int]
    username: str


@component
class User:
    users_repo: interfaces.UsersRepo
    publisher: Publisher

    @join_point
    @validate_arguments
    def get_users(self):
        users = self.users_repo.get_users()
        if not users:
            raise DoesNotExists
        return users

    @join_point
    @validate_arguments
    def delete_user(self, id):
        try:
            self.users_repo.get_user(id)
        except Exception:
            raise DoesNotExists
        self.users_repo.delete_user(id)

    @join_point
    @validate_arguments
    def get_user(self, id):
        users = self.users_repo.get_user(id)
        if not users:
            raise DoesNotExists
        return users

    @join_point
    @validate_arguments
    def add_user(self, username):
        user = UserInfo(username=username).create_obj(dataclasses.User)
        self.users_repo.add_user(user)

        if self.publisher:
            self.publisher.plan(
                Message('test', {'event': 'add_user', 'created': datetime.now(),
                                 'book_id': None, 'user_id': user.id})
            )
