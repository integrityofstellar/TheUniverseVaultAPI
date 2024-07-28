from api.models.planet import Planet
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from api.public.galaxies.solar_systems.planets.moons import moons_router

planets_router = APIRouter(prefix="/{solar_system_id}/planets")


@planets_router.get("/")
async def get_planets(
    galaxy_id: PydanticObjectId,
    solar_system_id: PydanticObjectId,
    limit: int = 10,
    skip: int = 0,
):

    if limit > 50:
        limit = 50

    total_planets = await Planet.find(
        {
            "solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        }
    ).count()

    planets = await Planet.find(
        {
            "solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        },
        skip=skip,
        limit=limit,
    ).to_list()

    _planets = []

    for planet in planets:
        planet = planet.model_dump()
        planet["meta"]["galaxy_id"] = str(planet["meta"]["galaxy_id"])

        _planets.append(planet)

    return {
        "planets": _planets,
        "meta": {"total": total_planets, "skip": skip, "limit": limit},
    }


@planets_router.get("/{planet_id}")
async def get_planet(
    galaxy_id: PydanticObjectId,
    solar_system_id: PydanticObjectId,
    planet_id: PydanticObjectId,
):
    planet = await Planet.find_one(
        {
            "_id": planet_id,
            "solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        }
    )

    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")

    _planet = planet.model_dump()
    _planet["meta"]["galaxy_id"] = str(_planet["meta"]["galaxy_id"])

    return {"planet": _planet}


planets_router.include_router(moons_router)
