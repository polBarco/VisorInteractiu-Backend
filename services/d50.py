from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import d50
from utils.GeoJSONConverter import GeoJSONConverter

class d50Service:

    @staticmethod
    def get_d50_by_name(name: str, db: Session):
        d50_list = db.query(d50).filter(d50.name == name).all()
        if not d50_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="d50 not found")
        else:
            return GeoJSONConverter.convert_to_geojson_list(
                d50_list,
                "d50Collection",
                lambda d50: {
                    "name": d50.name,
                    "d50": d50.d50
                }
            )