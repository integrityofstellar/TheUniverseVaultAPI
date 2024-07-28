import datetime
from beanie import Document, PydanticObjectId


class Planet(Document):
    name: str
    description: str

    solar_system_id: PydanticObjectId

    gravity: float
    diameter: float
    mass: float
    rotation_period: float
    orbital_period: float

    has_atmosphere: bool
    terrain: str
    surface_water: float
    temperature_day: float
    temperature_night: float
    kernel: str
    age: float

    materials: list[str]

    has_life: bool
    has_ring_system: bool

    discovery_date: datetime.datetime
    discovery_method: str
    discovery_status: str
    discovered_by: str

    created_at: datetime.datetime
    updated_at: datetime.datetime

    meta: dict = {}

    class Settings:
        name = "planets"
