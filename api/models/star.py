import datetime
from beanie import Document, PydanticObjectId


class Star(Document):
    name: str
    description: str

    solar_system_id: PydanticObjectId

    type: str
    mass: float
    radius: float
    luminosity: float
    temperature: int
    age: float
    has_planetary_system: bool
    metallicity: float
    rotation_velocity: float

    discovery_date: datetime.datetime
    discovery_method: str
    discovery_status: str
    discovered_by: str

    created_at: datetime.datetime
    updated_at: datetime.datetime

    meta: dict = {}

    class Settings:
        name = "stars"
