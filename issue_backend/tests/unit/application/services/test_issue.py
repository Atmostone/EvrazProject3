from datetime import datetime

import pytest

from issue_backend.application.services import Issue


@pytest.fixture(scope='function')
def service(issues_repo):
    return Issue(
        issues_repo=issues_repo,
    )


def test__create_issue(service):
    case_data = {
        'event': 'take_book',
        'created': datetime.now(),
        'book_id': 1,
        'user_id': 1
    }
    assert service.create_issue(**case_data) is None

def test__get_issues(service, issue):
    assert service.get_issues() == [issue, ]