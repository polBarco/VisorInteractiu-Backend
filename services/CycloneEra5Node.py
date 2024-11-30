from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import CycloneEra5Node
from utils.GeoJSONConverter import GeoJSONConverter

class CycloneEra5NodeService:

    @staticmethod
    def get_all_cyclone_era5_node(db: Session):
        cyclone_era5_node_list = db.query(CycloneEra5Node).all()
        if not cyclone_era5_node_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cyclone era5 node not found")
        else:
            return GeoJSONConverter.convert_to_geojson_list(
                cyclone_era5_node_list,
                "CycloneEra5NodeCollection",
                lambda node: {
                    "id": node.id
                }
            ) 