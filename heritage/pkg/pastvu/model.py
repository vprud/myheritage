import orjson
from pydantic import BaseModel


class GeoPoint(BaseModel):
    latitude: float = 55.824322
    longitude: float = 37.611089


class Photo(BaseModel):
    geo: GeoPoint
    title: str
    source: str
    period: str
    file_name: str
    cid: int


class Params(BaseModel):
    geo: GeoPoint = GeoPoint()
    distance: int = 125
    limit: int = 5
    skip: int = 0

    def set_pagination(self, page: int = 0) -> Params:
        self.skip = page * self.limit
        return self

    def to_api_params(self) -> str:
        """Serialize params for Pastvu API (geo as [lat, lon])."""
        payload = {
            "geo": [self.geo.latitude, self.geo.longitude],
            "distance": self.distance,
            "limit": self.limit,
            "skip": self.skip,
        }
        return orjson.dumps(payload).decode()
