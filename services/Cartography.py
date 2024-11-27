from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import Cartography
from utils.GeoJSONConverter import GeoJSONConverter
# from pyproj import Transformer
# from geoalchemy2.shape import to_shape
# from shapely.ops import transform
# from shapely.geometry import mapping

class CartographyService:
        
    @staticmethod
    def get_cartography_by_element(element: str, db: Session):
        cartography_list = db.query(Cartography).filter(Cartography.element == element).all()
        if not cartography_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cartography not found")
        else:
            return GeoJSONConverter.convert_to_geojson_list(
                objects_list=cartography_list,
                collection_type="CartographyCollection",
                properties_func=lambda x: {
                    "element": x.element,
                    "area_m2": x.area_m2,
                    "area_km2": x.area_km2,
                    "longitud": x.longitud,
                    "perimet_km": x.perimet_km,
                },
                simplify_tolerance=0.001,  # Apply simplification
            )
    

# def convert_to_geojson_list(cartography_list: list) -> dict:
#     # Configura el transformador UTM a WGS84
#     transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)

#     features = []

#     for cartography in cartography_list:
#         # Convierte la geometría a un objeto Shapely
#         geom = to_shape(cartography.geom)

#         # Convierte las coordenadas de UTM a WGS84
#         wgs84_geom = transform(transformer.transform, geom)

#         # Simplifica la geometría
#         simplified_geom = wgs84_geom.simplify(0.001, preserve_topology=True)

#         # Agrega la geometría simplificada al array de features
#         feature = {
#             "type": "Feature",
#             "properties": {
#                 "element": cartography.element,
#                 "area_m2": cartography.area_m2,
#                 "area_km2": cartography.area_km2,
#                 "longitud": cartography.longitud,
#                 "perimet_km": cartography.perimet_km
#             },
#             "geometry": mapping(simplified_geom)
#         }
#         features.append(feature)

#     # Formatear todos los registros como una colección de características
#     geojson = {
#         "type": "CartographyCollection",
#         "features": features
#     }
    
#     return geojson
