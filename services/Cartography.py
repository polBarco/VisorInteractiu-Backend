from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import Cartography
from pyproj import Transformer
from geoalchemy2.shape import to_shape
from shapely.ops import transform
from shapely.geometry import mapping

class CartographyService:
        
    @staticmethod
    def get_cartography_by_element(element: str, db: Session):
        cartography_list = db.query(Cartography).filter(Cartography.element == element).all()
        if not cartography_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cartography not found")
        else:
            return convert_to_geojson_list(cartography_list)
        
def round_coordinates(geometry, precision=5):
    """Función para redondear las coordenadas de una geometría."""
    def rounder(x, y, z=None):
        return (round(x, precision), round(y, precision)) if z is None else (round(x, precision), round(y, precision), round(z, precision))
    
    return transform(rounder, geometry)

def convert_to_geojson_list(cartography_list: list) -> dict:
    # Configura el transformador UTM a WGS84
    transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)

    features = []

    for cartography in cartography_list:
        # Convierte la geometría a un objeto Shapely
        geom = to_shape(cartography.geom)

        # Convierte las coordenadas de UTM a WGS84 después de simplificar
        wgs84_geom = transform(transformer.transform, geom)
        rounded_wgs84_geom = round_coordinates(wgs84_geom, precision=6)

        simplified_geom = rounded_wgs84_geom.simplify(0.001, preserve_topology=True)

        # Agrega la geometría simplificada al array de features
        feature = {
            "type": "Feature",
            "properties": {
                "element": cartography.element,
                "area_m2": cartography.area_m2,
                "area_km2": cartography.area_km2,
                "longitud": cartography.longitud,
                "perimet_km": cartography.perimet_km
            },
            "geometry": mapping(simplified_geom)
        }
        features.append(feature)

    # Formatear todos los registros como una colección de características
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    return geojson
