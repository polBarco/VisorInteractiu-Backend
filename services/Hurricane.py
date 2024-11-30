from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import Hurricane
from utils.GeoJSONConverter import GeoJSONConverter

class HurricaneService:

    @staticmethod
    def get_hurricane_types(db: Session):
        hurricane_types = db.query(Hurricane.type).distinct().order_by(Hurricane.type.asc()).all()
        if not hurricane_types:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hurricane types not found")
        else:
            return [hurricane_type[0] for hurricane_type in hurricane_types]
        
    @staticmethod
    def get_hurricane_years_by_type(type: str, db: Session):
        hurricane_years = db.query(Hurricane.year).filter(Hurricane.type == type).distinct().order_by(Hurricane.year.asc()).all()
        if not hurricane_years:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hurricane years not found")
        else:
            return [hurricane_year[0] for hurricane_year in hurricane_years]
    
    @staticmethod
    def get_hurricane_by_type_and_year(type: str, year: int, db: Session):
        hurricane_list = db.query(Hurricane).filter(Hurricane.type == type, Hurricane.year == year).all()
        if not hurricane_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hurricane not found")
        else:
            return GeoJSONConverter.convert_to_geojson_list(
                hurricane_list,
                "HurricaneCollection",
                lambda hurricane: {
                    "name": hurricane.name,
                    "year": hurricane.year,
                    "type": hurricane.type
                }
            )