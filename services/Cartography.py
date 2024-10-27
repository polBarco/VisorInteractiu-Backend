from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.models import Cartography
from pyproj import Transformer
from geoalchemy2.shape import to_shape
from shapely.ops import transform
from shapely.geometry import mapping

class CartographyService:

    @staticmethod
    def get_cartography(gid: int, db: Session):
        cartography = db.query(Cartography).filter(Cartography.gid == gid).first()
        if not cartography:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cartography not found")
        else:
            return convert_to_geojson(cartography)
        
def convert_to_geojson(cartography: Cartography) -> dict:
    transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)
    utm_geom = to_shape(cartography.geom)
    lon_lat_geom = transform(transformer.transform, utm_geom)

    geojson = {
        "element": cartography.element,
        "geometry": mapping(lon_lat_geom),
        "properties": {
            "area_m2": cartography.area_m2,
            "area_km2": cartography.area_km2,
            "longitud": cartography.longitud,
            "perimet_km": cartography.perimet_km
        }
    }
    return geojson