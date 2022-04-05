from typing import Optional

import attr


@attr.dataclass
class Book:
    title: str
    text: str
    id: Optional[int] = None
