from abc import ABC, abstractmethod
from typing import Optional

from application.dataclasses import Issue


class IssueRepo(ABC):
    @abstractmethod
    def add_issue(self, issue):
        ...
    @abstractmethod
    def get_issues(self):
        ...


