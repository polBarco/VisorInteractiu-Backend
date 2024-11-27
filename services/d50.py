from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import d50
from utils.GeoJSONConverter import GeoJSONConverter
# from pyproj import Transformer
# from geoalchemy2.shape import to_shape
# from shapely.ops import transform
# from shapely.geometry import mapping

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


# def convert_to_geojson_list(d50_list: list) -> dict:
#     # Configura el transformador UTM a WGS84
#     transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)

#     features = []

#     for d50 in d50_list:
#         # Convierte la geometría a un objeto Shapely
#         geom = to_shape(d50.geom)

#         # Convierte las coordenadas de UTM a WGS84 después de simplificar
#         wgs84_geom = transform(transformer.transform, geom)

#         # Agrega la geometría simplificada al array de features
#         feature = {
#             "properties": {
#                 "name": d50.name,
#                 "d50": d50.d50,
#             },
#             "geometry": mapping(wgs84_geom)
#         }
#         features.append(feature)

#     # Formatear todos los registros como una colección de características
#     geojson = {
#         "type": "d50Collection",
#         "features": features
#     }
    
#     return geojson