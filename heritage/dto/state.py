from dataclasses import asdict, dataclass

import orjson


@dataclass
class SearchState:
    latitude: float = 55.824322
    longitude: float = 37.611089
    page: int = 1

    def __str__(self) -> str:
        return orjson.dumps(self).decode("utf-8")

    def to_dict(self) -> dict[str, float | int]:
        return asdict(self)

    def shift(self) -> None:
        self.page += 1
