from fastapi import APIRouter, HTTPException
from api.schemas.response import OkResponse
from api.schemas.galaxy import DetailedGalaxyResponseSchema
from api.models.moon import Moon
from api.models.planet import Planet
from api.models.star import Star
from api.models.solar_system import SolarSystem
from api.models.galaxy import Galaxy
from beanie import PydanticObjectId


galaxies_router = APIRouter(prefix="/galaxies")


@galaxies_router.get("/")
async def get_galaxies(limit: int = 10, skip: int = 0) -> OkResponse:
    if limit > 50:
        limit = 50
    total_galaxies = await Galaxy.count()
    galaxies = await Galaxy.find_all(skip=skip, limit=limit).to_list()
    return OkResponse(
        data={"galaxies": galaxies},
        meta={
            "total": total_galaxies,
            "skip": skip,
            "limit": limit,
        },
    )


@galaxies_router.get("/{galaxy_id}")
async def get_galaxy(galaxy_id: PydanticObjectId) -> OkResponse:
    galaxy = await Galaxy.get(galaxy_id)
    if not galaxy:
        raise HTTPException(status_code=404, detail="Galaxy not found")

    solar_systems_count = await SolarSystem.find({"galaxy_id": galaxy_id}).count()
    stars_count = await Star.find({"meta.galaxy_id": galaxy_id}).count()
    planets_count = await Planet.find({"meta.galaxy_id": galaxy_id}).count()
    moons_count = await Moon.find({"meta.galaxy_id": galaxy_id}).count()

    _response = DetailedGalaxyResponseSchema(
        id=str(galaxy_id),
        name=galaxy.name,
        description=galaxy.description,
        type=galaxy.type,
        mass=galaxy.mass,
        diameter=galaxy.diameter,
        number_of_stars=galaxy.number_of_stars,
        distance_from_earth=galaxy.distance_from_earth,
        has_supermassive_black_hole=galaxy.has_supermassive_black_hole,
        metallicity=galaxy.metallicity,
        velocity=galaxy.velocity,
        discovery_date=galaxy.discovery_date,
        discovery_method=galaxy.discovery_method,
        discovery_status=galaxy.discovery_status,
        discovered_by=galaxy.discovered_by,
        created_at=galaxy.created_at,
        updated_at=galaxy.updated_at,
        solar_systems_in_db=solar_systems_count,
        stars_in_db=stars_count,
        planets_in_db=planets_count,
        moons_in_db=moons_count,
    )

    return OkResponse(data={"galaxy": _response})
