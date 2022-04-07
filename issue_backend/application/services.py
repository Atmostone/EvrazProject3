from datetime import datetime
from typing import Optional

from classic.app import DTO
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from application import interfaces, dataclasses

join_points = PointCut()
join_point = join_points.join_point


class IssueInfo(DTO):
    id: Optional[int]
    event: str
    created: datetime
    book_id: Optional[int] = None
    user_id: Optional[int] = None


@component
class Issue:
    issues_repo: interfaces.IssueRepo

    def create_issue(self, event, created, book_id, user_id):
        issue = IssueInfo(event=event, created=created, book_id=book_id, user_id=user_id).create_obj(dataclasses.Issue)
        self.issues_repo.add_issue(issue)

    @join_point
    @validate_arguments
    def get_issues(self):
        issues = self.issues_repo.get_issues()
        if not issues:
            raise Exception
        return issues
