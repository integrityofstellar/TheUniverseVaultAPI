import datetime
from beanie import Document, PydanticObjectId


class SolarSystem(Document):
    name: str
    description: str

    galaxy_id: PydanticObjectId  # Reference to the galaxy the solar system belongs to

    age: float  # Age of the solar system in billion years
    distance_from_earth: float  # Distance from Earth in light-years

    has_life: bool  # Whether any life forms have been detected in the solar system
    habitable_zones: int  # Number of habitable zones in the solar system

    discovery_date: datetime.datetime
    discovery_method: str
    discovery_status: str
    discovered_by: str

    created_at: datetime.datetime
    updated_at: datetime.datetime

    meta: dict = {}

    class Settings:
        name = "solar_systems"
