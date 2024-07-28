from fastapi import APIRouter, HTTPException
from datetime import datetime
from beanie import PydanticObjectId
from api.models.solar_system import SolarSystem
from api.models.galaxy import Galaxy
from api.schemas.response import OkResponse
from api.models.planet import Planet
from api.schemas.planet import CreatePlanetSchema
from api.private.galaxies.solar_systems.planets.moons import moons_router


planets_router = APIRouter(prefix="/{solar_system_id}/planets")


@planets_router.post("/")
async def new_planet(
    solar_system_id: PydanticObjectId,
    galaxy_id: PydanticObjectId,
    planet_payload: CreatePlanetSchema,
) -> OkResponse:

    _galaxy = await Galaxy.get(galaxy_id)
    if not _galaxy:
        raise HTTPException(status_code=404, detail="Galaxy not found")

    _solar_system = await SolarSystem.get(solar_system_id)
    if not _solar_system:
        raise HTTPException(status_code=404, detail="Solar System not found")

    if await Planet.find_one({"name": planet_payload.name}):
        raise HTTPException(status_code=400, detail="Planet already exists")

    planet = Planet(
        **planet_payload.model_dump(),
        solar_system_id=solar_system_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        meta={
            "galaxy_id": galaxy_id,
        }
    )

    await planet.insert()

    _planet = planet.model_dump()
    _planet["meta"]["galaxy_id"] = str(_planet["meta"]["galaxy_id"])

    return OkResponse(
        detail="Planet created",
        data=_planet,
    )


planets_router.include_router(moons_router)
