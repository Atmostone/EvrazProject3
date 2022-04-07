from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select

from application.interfaces import IssueRepo
from application.dataclasses import Issue


@component
class IssueRepo(BaseRepository, IssueRepo):
    def add_issue(self, issue):
        self.session.add(issue)
        self.session.commit()
        return issue.id

    def get_issues(self) -> Optional[Issue]:
        query = select(Issue)
        return self.session.execute(query).scalars().all()
