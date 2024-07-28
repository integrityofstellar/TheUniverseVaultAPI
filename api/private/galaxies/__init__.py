from fastapi import APIRouter, Depends, HTTPException
from beanie import PydanticObjectId
import datetime
from api.models.galaxy import Galaxy
from api.schemas.galaxy import CreateGalaxySchema
from api.schemas.response import OkResponse

from .solar_systems import solar_systems_router

galaxy_router = APIRouter(prefix="/galaxies")


@galaxy_router.post("/", response_model=OkResponse)
async def create_galaxy(galaxy_payload: CreateGalaxySchema) -> OkResponse:
    # validation
    if await Galaxy.find_one({"name": galaxy_payload.name}):
        raise HTTPException(status_code=400, detail="Galaxy already exists")

    galaxy = Galaxy(
        **galaxy_payload.model_dump(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

    await galaxy.insert()

    return OkResponse(detail="Galaxy created", data=galaxy.model_dump())


galaxy_router.include_router(solar_systems_router)
