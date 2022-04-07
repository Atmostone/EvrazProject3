from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class Issue:
    event: str
    created: datetime
    id: Optional[int] = None
    book_id: Optional[int] = None
    user_id: Optional[int] = None
