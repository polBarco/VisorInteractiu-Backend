from pydantic import BaseModel

class HurricaneBase(BaseModel):
    name: str
    year: int
    type: str

class HurricaneGeoJSON(BaseModel):
    geom: dict
    properties: HurricaneBase

    class Config:
        from_attributes = True