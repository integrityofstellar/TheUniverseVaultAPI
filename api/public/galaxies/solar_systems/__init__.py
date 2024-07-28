from api.models.solar_system import SolarSystem
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from api.public.galaxies.solar_systems.stars import stars_router
from api.public.galaxies.solar_systems.planets import planets_router


solar_systems_router = APIRouter(prefix="/{galaxy_id}/solar-systems")


@solar_systems_router.get("/")
async def get_solar_systems(
    galaxy_id: PydanticObjectId, limit: int = 10, skip: int = 0
):
    if not await SolarSystem.find_one({"galaxy_id": galaxy_id}):
        raise HTTPException(status_code=404, detail="Galaxy not found")

    if limit > 50:
        limit = 50
    total_solar_systems = await SolarSystem.find({"galaxy_id": galaxy_id}).count()

    solar_systems = await SolarSystem.find(
        {"galaxy_id": galaxy_id}, skip=skip, limit=limit
    ).to_list()
    return {
        "solar_systems": solar_systems,
        "meta": {"total": total_solar_systems, "skip": skip, "limit": limit},
    }


@solar_systems_router.get("/{solar_system_id}")
async def get_solar_system(
    galaxy_id: PydanticObjectId, solar_system_id: PydanticObjectId
):
    solar_system = await SolarSystem.find_one(
        {"_id": solar_system_id, "galaxy_id": galaxy_id}
    )
    if not solar_system:
        raise HTTPException(status_code=404, detail="Solar system not found")
    return {"solar_system": solar_system}


solar_systems_router.include_router(stars_router)
solar_systems_router.include_router(planets_router)
