from pydantic import BaseModel

class CycloneSedimentTransportBase(BaseModel):
    id: int
    transport: float
    percent: float

class CycloneSedimentTransporGeoJSON(BaseModel):
    geom: dict
    properties: CycloneSedimentTransportBase

    class Config:
        from_attributes = True