from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select

from application.interfaces import UsersRepo
from application.dataclasses import User


@component
class UsersRepo(BaseRepository, UsersRepo):
    def get_users(self) -> Optional[User]:
        query = select(User)
        return self.session.execute(query).scalars().all()

    def add_user(self, user):
        self.session.add(user)
        self.session.flush()
        return user.id
