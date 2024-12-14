from pydantic import BaseModel

class RiversMozambiqueBase(BaseModel):
    arcid: int
    up_cells: int
    region: str

class RiversMozambiqueGeoJSON(BaseModel):
    geom: dict
    properties: RiversMozambiqueBase

    class Config:
        from_attributes = True