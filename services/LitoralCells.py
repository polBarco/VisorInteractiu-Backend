from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import LitoralCells
from utils.GeoJSONConverter import GeoJSONConverter
# from pyproj import Transformer
# from geoalchemy2.shape import to_shape
# from shapely.ops import transform
# from shapely.geometry import mapping

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
        

# def convert_to_geojson_list(litoral_cells_list: list) -> dict:
#     # Configura el transformador UTM a WGS84
#     transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)

#     features = []

#     for litoral_cells in litoral_cells_list:
#         # Convierte la geometría a un objeto Shapely
#         geom = to_shape(litoral_cells.geom)

#         # Convierte las coordenadas de UTM a WGS84 después de simplificar
#         wgs84_geom = transform(transformer.transform, geom)    

#         # Agrega la geometría simplificada al array de features
#         feature = {
#             "properties": {
#                 "name": litoral_cells.name,
#                 "length": litoral_cells.length,
#                 "length_km": litoral_cells.length_km,
#                 "coord_xfin": litoral_cells.coord_xfin,
#                 "coord_yfin": litoral_cells.coord_yfin,
#                 "coord_yini": litoral_cells.coord_yini,
#                 "coord_xini": litoral_cells.coord_xini,
#                 "par_impar": litoral_cells.par_impar
#             },
#             "geometry": mapping(wgs84_geom)
#         }
#         features.append(feature)

#     # Formatear todos los registros como una colección de características
#     geojson = {
#         "type": "LitoralCellsCollection",
#         "features": features
#     }
    
#     return geojson