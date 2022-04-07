from classic.components import component

from .join_points import join_point
from application import services


@component
class Issue:
    issue: services.Issue

    @join_point
    def on_get_issues(self, request, response):
        issues = self.issue.get_issues()
        response.media = {
            'issue': str(issues),
        }

