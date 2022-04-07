from datetime import datetime

import pytest

from issue_backend.application import dataclasses


@pytest.fixture
def issue():
    return dataclasses.Issue(
        id=1,
        event='take_book',
        created=datetime.now(),
        book_id=1,
        user_id=1
    )