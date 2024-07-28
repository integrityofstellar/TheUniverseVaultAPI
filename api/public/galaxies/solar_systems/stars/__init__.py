from api.models.star import Star
from api.models.solar_system import SolarSystem
from api.models.galaxy import Galaxy
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException


stars_router = APIRouter(prefix="/{solar_system_id}/stars")


@stars_router.get("/")
async def get_stars(
    galaxy_id: PydanticObjectId,
    solar_system_id: PydanticObjectId,
    limit: int = 10,
    skip: int = 0,
):

    if not await Star.find_one(
        {"solar_system_id": solar_system_id, "meta.galaxy_id": galaxy_id}
    ):
        raise HTTPException(status_code=404, detail="Solar system not found")

    if limit > 50:
        limit = 50

    total_stars = await Star.find(
        {
            "solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        }
    ).count()

    stars = await Star.find(
        {
            "solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        },
        skip=skip,
        limit=limit,
    ).to_list()

    _stars = []

    for star in stars:
        star = star.model_dump()
        star["meta"]["galaxy_id"] = str(star["meta"]["galaxy_id"])
        _stars.append(star)

    return {
        "stars": _stars,
        "meta": {"total": total_stars, "skip": skip, "limit": limit},
    }


@stars_router.get("/{star_id}")
async def get_star(
    galaxy_id: PydanticObjectId,
    solar_system_id: PydanticObjectId,
    star_id: PydanticObjectId,
):
    star = await Star.find_one(
        {
            "_id": star_id,
            "solar_system_id": solar_system_id,
            "meta.galaxy_id": galaxy_id,
        }
    )
    if not star:
        raise HTTPException(status_code=404, detail="Star not found")

    _star = star.model_dump()
    _star["meta"]["galaxy_id"] = str(_star["meta"]["galaxy_id"])

    return {"star": _star}
