from fastapi import APIRouter
from api.private.galaxies import galaxy_router


# ToDo: Implement Authorization and Authentication
private_router = APIRouter(prefix="/private")

private_router.include_router(galaxy_router)
