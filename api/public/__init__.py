from fastapi import APIRouter
from api.public.galaxies import galaxies_router

public_router = APIRouter(prefix="/public")

public_router.include_router(galaxies_router)
