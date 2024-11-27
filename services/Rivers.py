from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import Rivers
from utils.GeoJSONConverter import GeoJSONConverter
# from pyproj import Transformer
# from geoalchemy2.shape import to_shape
# from shapely.ops import transform
# from shapely.geometry import mapping

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
        

# def convert_to_geojson_list(rivers_list: list) -> dict:
#     # Configura el transformador UTM a WGS84
#     transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)

#     features = []

#     for rivers in rivers_list:
#         # Convierte la geometría a un objeto Shapely
#         geom = to_shape(rivers.geom)

#         # Convierte las coordenadas de UTM a WGS84 después de simplificar
#         wgs84_geom = transform(transformer.transform, geom)

#         # Agrega la geometría simplificada al array de features
#         feature = {
#             "properties": {
#                 "arcid": rivers.arcid,
#                 "up_cells": rivers.up_cells
#             },
#             "geometry": mapping(wgs84_geom)
#         }
#         features.append(feature)

#     # Formatear todos los registros como una colección de características
#     geojson = {
#         "type": "RiversCollection",
#         "features": features
#     }
    
#     return geojson