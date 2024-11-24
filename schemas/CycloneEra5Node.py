from pydantic import BaseModel

class CycloneEra5NodeBase(BaseModel):
    id: int

class CycloneEra5NodeGeoJSON(BaseModel):
    geom: dict
    property: CycloneEra5NodeBase

    class Config:
        from_attributes = True