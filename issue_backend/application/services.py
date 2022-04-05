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
    title: str
    text: str

@component
class Issue:
    issues_repo: interfaces.IssueRepo

