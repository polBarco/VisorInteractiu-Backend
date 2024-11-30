from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import Rivers
from utils.GeoJSONConverter import GeoJSONConverter

class RiversService:

    @staticmethod
    def get_all_rivers(db: Session):
        rivers_list = db.query(Rivers).all()
        if not rivers_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rivers not found")
        else:
            return GeoJSONConverter.convert_to_geojson_list(
                rivers_list,
                "RiversCollection",
                lambda r: {
                    "arcid": r.arcid,
                    "up_cells": r.up_cells
                }
            )