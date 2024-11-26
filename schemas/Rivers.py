from pydantic import BaseModel

class RiversBase(BaseModel):
    arcid: int
    up_cells: int

class RiversGeoJSON(BaseModel):
    geom: dict
    properties: RiversBase

    class Config:
        from_attributes = True