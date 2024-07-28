from fastapi import APIRouter, HTTPException
from datetime import datetime
from beanie import PydanticObjectId
from api.models.solar_system import SolarSystem
from api.models.galaxy import Galaxy
from api.models.star import Star
from api.schemas.response import OkResponse
from api.schemas.star import CreateStarSchema


stars_router = APIRouter(prefix="/{solar_system_id}/stars")


@stars_router.post("/")
async def new_star(
    solar_system_id: PydanticObjectId,
    galaxy_id: PydanticObjectId,
    star_payload: CreateStarSchema,
) -> OkResponse:

    # ToDo: add middleware to check galaxy and solar system existence before reaching this point, to reduce the number of queries
    _galaxy = await Galaxy.get(galaxy_id)
    if not _galaxy:
        raise HTTPException(status_code=404, detail="Galaxy not found")

    _solar_system = await SolarSystem.get(solar_system_id)
    if not _solar_system:
        raise HTTPException(status_code=404, detail="Solar System not found")

    if await Star.find_one({"name": star_payload.name}):
        raise HTTPException(status_code=400, detail="Star already exists")

    star = Star(
        **star_payload.model_dump(),
        solar_system_id=solar_system_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        meta={
            "galaxy_id": galaxy_id,
        }
    )

    await star.insert()

    _star = star.model_dump()
    _star["meta"]["galaxy_id"] = str(_star["meta"]["galaxy_id"])

    return OkResponse(
        detail="Star created",
        data=_star,
    )
