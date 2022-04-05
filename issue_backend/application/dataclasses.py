from typing import Optional

import attr


@attr.dataclass
class Issue:
    title: str
    text: str
    id: Optional[int] = None
