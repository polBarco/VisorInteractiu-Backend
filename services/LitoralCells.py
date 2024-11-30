from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import LitoralCells
from utils.GeoJSONConverter import GeoJSONConverter

class LitoralCellsService:

    @staticmethod
    def get_litoral_cells_by_name(name: str, db: Session):
        litoral_cells_list = db.query(LitoralCells).filter(LitoralCells.name == name).all()
        if not litoral_cells_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="LitoralCells not found")
        else:
            return GeoJSONConverter.convert_to_geojson_list(
                litoral_cells_list,
                "LitoralCellsCollection",
                lambda l: {
                    "name": l.name,
                    "length": l.length,
                    "length_km": l.length_km,
                    "coord_xfin": l.coord_xfin,
                    "coord_yfin": l.coord_yfin,
                    "coord_xini": l.coord_xini,
                    "coord_yini": l.coord_yini,
                    "par_impar": l.par_impar
                }
            )