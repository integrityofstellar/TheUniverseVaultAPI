from pydantic import BaseModel, field_validator
import datetime


class DetailedGalaxyResponseSchema(BaseModel):
    id: str
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

    solar_systems_in_db: int
    stars_in_db: int
    planets_in_db: int
    moons_in_db: int


class CreateGalaxySchema(BaseModel):
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

    @field_validator("type")
    def validate_type(cls, v):
        if v.lower() not in [
            "spiral",
            "elliptical",
            "lenticular",
            "irregular",
            "active",
            "seyfert",
            "quasar",
            "blazar",
            "starburst",
            "dwarf",
            "barred spiral",
        ]:
            raise ValueError("Invalid galaxy type")
        return v
