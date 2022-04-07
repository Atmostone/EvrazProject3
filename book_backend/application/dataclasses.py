from typing import Optional

import attr


@attr.dataclass
class Book:
    title: str
    description: str
    user_id: Optional[int] = None
    id: Optional[int] = None
