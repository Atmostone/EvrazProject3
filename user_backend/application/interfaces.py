from abc import ABC, abstractmethod
from typing import Optional

from application.dataclasses import User


class UsersRepo(ABC):
    @abstractmethod
    def get_users(self) -> Optional[User]:
        ...

    @abstractmethod
    def add_user(self, user):
        ...
