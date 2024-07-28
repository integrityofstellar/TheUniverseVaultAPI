from pydantic import BaseModel
import datetime
from beanie import PydanticObjectId


class CreateStarSchema(BaseModel):
    name: str
    description: str

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
