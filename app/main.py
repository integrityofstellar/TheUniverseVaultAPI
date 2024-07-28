from fastapi import FastAPI
from beanie import init_beanie
from app.core.database import db

from api.models import moon, star, galaxy, planet, solar_system

from api.router import api_router

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_beanie(
        database=db,
        document_models=[
            moon.Moon,
            star.Star,
            galaxy.Galaxy,
            planet.Planet,
            solar_system.SolarSystem,
        ],
    )


app.include_router(api_router)
