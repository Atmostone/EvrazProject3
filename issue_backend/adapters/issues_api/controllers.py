from classic.components import component

from .join_points import join_point
from application import services


@component
class Issue:
    issue: services.Issue

    @join_point
    def on_get_issues(self, request, response):
        issues = self.issue.get_issues()
        response.media = [{
            'id': issue.id,
            'event': issue.event,
            'created': str(issue.created),
            'user_id': issue.user_id,
            'book_id': issue.book_id,
        } for issue in issues]
