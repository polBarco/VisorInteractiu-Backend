from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import Cartography
from utils.GeoJSONConverter import GeoJSONConverter

class CartographyService:
        
    @staticmethod
    def get_cartography_by_element(element: str, db: Session):
        cartography_list = db.query(Cartography).filter(Cartography.element == element).all()
        if not cartography_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cartography not found")
        else:
            return GeoJSONConverter.convert_to_geojson_list(
                objects_list=cartography_list,
                collection_type="CartographyCollection",
                properties_func=lambda x: {
                    "element": x.element,
                    "area_m2": x.area_m2,
                    "area_km2": x.area_km2,
                    "longitud": x.longitud,
                    "perimet_km": x.perimet_km,
                },
                simplify_tolerance=0.001,  # Apply simplification
            )
