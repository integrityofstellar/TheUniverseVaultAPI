from api.models.star import Star
from api.models.planet import Planet
from api.models.moon import Moon
from api.models.solar_system import SolarSystem
from api.models.galaxy import Galaxy
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException


moons_router = APIRouter(prefix="/{planet_id}/moons")


@moons_router.get("/")
async def get_moons(
    galaxy_id: PydanticObjectId,
    solar_system_id: PydanticObjectId,
    planet_id: PydanticObjectId,
    limit: int = 10,
    skip: int = 0,
):

    if limit > 50:
        limit = 50

    total_moons = await Moon.find(
        {
            "planet_id": planet_id,
            "meta.solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        }
    ).count()

    moons = await Moon.find(
        {
            "planet_id": planet_id,
            "meta.solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        },
        skip=skip,
        limit=limit,
    ).to_list()

    _moons = []

    for moon in moons:
        moon = moon.model_dump()
        moon["meta"]["galaxy_id"] = str(moon["meta"]["galaxy_id"])
        moon["meta"]["solar_system_id"] = str(moon["meta"]["solar_system_id"])
        _moons.append(moon)

    return {
        "moons": _moons,
        "meta": {"total": total_moons, "skip": skip, "limit": limit},
    }


@moons_router.get("/{moon_id}")
async def get_moon(
    galaxy_id: PydanticObjectId,
    solar_system_id: PydanticObjectId,
    planet_id: PydanticObjectId,
    moon_id: PydanticObjectId,
):
    moon = await Moon.find_one(
        {
            "_id": moon_id,
            "planet_id": planet_id,
            "meta.solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        }
    )
    if not moon:
        raise HTTPException(status_code=404, detail="Moon not found")

    _moon = moon.model_dump()
    _moon["meta"]["galaxy_id"] = str(_moon["meta"]["galaxy_id"])
    _moon["meta"]["solar_system_id"] = str(_moon["meta"]["solar_system_id"])

    return {"moon": _moon}
