from typing import Optional

import attr


@attr.dataclass
class User:
    username: str
    id: Optional[int] = None
