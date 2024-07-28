import datetime
from beanie import Document, PydanticObjectId


class Moon(Document):
    name: str
    description: str

    planet_id: PydanticObjectId

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

    discovery_date: datetime.datetime
    discovery_method: str
    discovery_status: str
    discovered_by: str

    created_at: datetime.datetime
    updated_at: datetime.datetime

    meta: dict = {}

    class Settings:
        name = "moons"
