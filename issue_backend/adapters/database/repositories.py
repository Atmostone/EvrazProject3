from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select

from application.interfaces import IssueRepo
from application.dataclasses import Issue


@component
class IssueRepo(BaseRepository, IssueRepo):
    pass