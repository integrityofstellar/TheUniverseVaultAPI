from pydantic import BaseModel


class OkResponse(BaseModel):
    detail: str = "success"
    data: dict = {}
    meta: dict = {}
