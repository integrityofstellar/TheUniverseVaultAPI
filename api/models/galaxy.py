import datetime
from beanie import Document, PydanticObjectId


class Galaxy(Document):
    name: str
    description: str

    type: str
    mass: float
    diameter: float
    number_of_stars: int
    distance_from_earth: float

    has_supermassive_black_hole: bool
    metallicity: float
    velocity: float

    discovery_date: datetime.datetime
    discovery_method: str
    discovery_status: str
    discovered_by: str

    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Settings:
        name = "galaxies"
