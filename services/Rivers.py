from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import asc, func
from core.models import Rivers
from utils.GeoJSONConverter import GeoJSONConverter

class RiversService:

    @staticmethod
    def get_paginated_rivers(page: int, limit: int, db: Session):
        offset = (page - 1) * limit  # offset for pagination
        
        # Ordenar los resultados por `arcid` para asegurar consistencia en la paginación
        rivers_query = db.query(
            Rivers.arcid, 
            Rivers.up_cells, 
            Rivers.geom  
        ).order_by(asc(Rivers.arcid)).offset(offset).limit(limit)
        
        rivers_list = rivers_query.all()

        total = db.query(func.count(Rivers.arcid)).scalar() #total elements

        rivers_geojson = GeoJSONConverter.convert_rivers_to_geojson_list(rivers_list, "FeatureCollection", lambda obj: {
            "arcid": obj.arcid,
            "up_cells": obj.up_cells
        })

        return rivers_geojson, total