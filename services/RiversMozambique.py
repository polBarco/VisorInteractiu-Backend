from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import RiversMozambique
from utils.GeoJSONConverter import GeoJSONConverter

class RiversMozambiqueService:

    @staticmethod
    def get_rivers_by_region(region: str, db: Session):
        rivers_list = db.query(RiversMozambique).filter(RiversMozambique.region == region).all()
        if not rivers_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rivers not found")
        else:
            return GeoJSONConverter.convert_rivers_to_geojson_list(
                rivers_list,
                "RiversMozambiqueCollection",
                lambda r: {
                    "region": r.region,
                    "arcid": r.arcid,
                    "up_cells": r.up_cells
                }
            )