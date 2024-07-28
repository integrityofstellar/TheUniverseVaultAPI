import datetime
from beanie import Document, PydanticObjectId
from pydantic import BaseModel


class CreateSolarSystemSchema(BaseModel):
    name: str
    description: str

    age: float
    distance_from_earth: float

    has_life: bool
    habitable_zones: int

    discovery_date: datetime.datetime
    discovery_method: str
    discovery_status: str
    discovered_by: str
