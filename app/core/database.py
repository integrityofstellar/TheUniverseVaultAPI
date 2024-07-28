from beanie import PydanticObjectId, init_beanie, Document
import motor.motor_asyncio
from app.core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.DATABASE_URL, uuidRepresentation="standard"
)
db = client[settings.DATABASE_NAME]
