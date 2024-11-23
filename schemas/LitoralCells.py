from pydantic import BaseModel

class LitoralCellsBase(BaseModel):
    length: float
    length_km: float
    coord_xfin: float
    coord_yfin: float
    coord_yini: float
    coord_xini: float
    par_impar: str

class LitoralCellsGeoJSON(BaseModel):
    name: str
    geom: dict
    properties: LitoralCellsBase

    class Config:
        from_attributes = True