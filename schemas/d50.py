from pydantic import BaseModel

class d50Base(BaseModel):
    d50: float

class d50GeoJSON(BaseModel):
    name: str
    geom: dict
    properties: d50Base

    class Config:
        from_attributes = True


