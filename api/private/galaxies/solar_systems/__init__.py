from fastapi import APIRouter, HTTPException
from datetime import datetime
from beanie import PydanticObjectId
from api.models.solar_system import SolarSystem
from api.models.galaxy import Galaxy
from api.schemas.response import OkResponse
from api.schemas.solar_system import CreateSolarSystemSchema
from api.private.galaxies.solar_systems.stars import stars_router
from api.private.galaxies.solar_systems.planets import planets_router

solar_systems_router = APIRouter(prefix="/{galaxy_id}/solar-systems")


@solar_systems_router.post("/")
async def new_solar_system(
    galaxy_id: PydanticObjectId, solar_system_payload: CreateSolarSystemSchema
) -> OkResponse:

    _galaxy = await Galaxy.get(galaxy_id)
    if not _galaxy:
        raise HTTPException(status_code=404, detail="Galaxy not found")

    if await SolarSystem.find_one({"name": solar_system_payload.name}):
        raise HTTPException(status_code=400, detail="Solar System already exists")

    solar_system = SolarSystem(
        **solar_system_payload.model_dump(),
        galaxy_id=galaxy_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    await solar_system.insert()

    return OkResponse(detail="Solar System created", data=solar_system.model_dump())


solar_systems_router.include_router(stars_router)
solar_systems_router.include_router(planets_router)
