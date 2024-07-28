from fastapi import APIRouter, HTTPException
from datetime import datetime
from beanie import PydanticObjectId
from api.models.solar_system import SolarSystem
from api.models.galaxy import Galaxy
from api.schemas.response import OkResponse
from api.models.planet import Planet
from api.models.moon import Moon
from api.schemas.moon import CreateMoonSchema
from api.schemas.planet import CreatePlanetSchema


moons_router = APIRouter(prefix="/{planet_id}/moons")


@moons_router.post("/")
async def new_moon(
    planet_id: PydanticObjectId,
    solar_system_id: PydanticObjectId,
    galaxy_id: PydanticObjectId,
    moon_payload: CreateMoonSchema,
) -> OkResponse:

    _galaxy = await Galaxy.get(galaxy_id)
    if not _galaxy:
        raise HTTPException(status_code=404, detail="Galaxy not found")

    _solar_system = await SolarSystem.get(solar_system_id)
    if not _solar_system:
        raise HTTPException(status_code=404, detail="Solar System not found")

    _planet = await Planet.get(planet_id)
    if not _planet:
        raise HTTPException(status_code=404, detail="Planet not found")

    if await Moon.find_one({"name": moon_payload.name}):
        raise HTTPException(status_code=400, detail="Moon already exists")

    moon = Moon(
        **moon_payload.model_dump(),
        planet_id=planet_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        meta={
            "galaxy_id": galaxy_id,
            "solar_system_id": solar_system_id,
        }
    )

    await moon.insert()

    _moon = moon.model_dump()
    _moon["meta"]["galaxy_id"] = str(_moon["meta"]["galaxy_id"])
    _moon["meta"]["solar_system_id"] = str(_moon["meta"]["solar_system_id"])

    return OkResponse(
        detail="Moon created",
        data=_moon,
    )
