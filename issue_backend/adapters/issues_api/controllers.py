from classic.components import component

from .join_points import join_point
from application import services


@component
class Issue:
    issue: services.Issue

