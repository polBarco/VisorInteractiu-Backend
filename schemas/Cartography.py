from pydantic import BaseModel

class CartographyBase(BaseModel):
    area_m2: float
    area_km2: float
    longitud: float
    perimet_km: float

class CartographyGeoJSON(BaseModel):
    element: str
    geom: dict
    properties: CartographyBase

    class Config:
        from_attributes = True
