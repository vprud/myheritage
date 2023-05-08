from dataclasses import dataclass


@dataclass
class SearchState:
    latitude: float = 55.824322
    longitude: float = 37.611089
    page: int = 1

    def shift(self) -> None:
        self.page += 1