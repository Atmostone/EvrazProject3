from unittest.mock import Mock

import pytest

from application import interfaces


@pytest.fixture(scope='function')
def issues_repo(issue):
    issues_repo = Mock(interfaces.IssueRepo)
    issues_repo.create_issue = Mock(return_value=None)
    issues_repo.get_issues = Mock(return_value=[issue, ])
    return issues_repo
