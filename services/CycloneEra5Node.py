from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import CycloneEra5Node
from pyproj import Transformer
from geoalchemy2.shape import to_shape
from shapely.ops import transform
from shapely.geometry import mapping

class CycloneEra5NodeService:

    @staticmethod
    def get_all_cyclone_era5_node(db: Session):
        cyclone_era5_node_list = db.query(CycloneEra5Node).all()
        if not cyclone_era5_node_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cyclone era5 node not found")
        else:
            return convert_to_geojson_list(cyclone_era5_node_list)
        
def round_coordinates(geometry, precision=5):
    """Función para redondear las coordenadas de una geometría."""
    def rounder(x, y, z=None):
        return (round(x, precision), round(y, precision)) if z is None else (round(x, precision), round(y, precision), round(z, precision))
    
    return transform(rounder, geometry)

def convert_to_geojson_list(cyclone_era5_node_list: list) -> dict:
    # Configura el transformador UTM a WGS84
    transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)

    features = []

    for cyclone_era5_node in cyclone_era5_node_list:
        # Convierte la geometría a un objeto Shapely
        geom = to_shape(cyclone_era5_node.geom)

        # Convierte las coordenadas de UTM a WGS84 después de simplificar
        wgs84_geom = transform(transformer.transform, geom)
        rounded_wgs84_geom = round_coordinates(wgs84_geom, precision=6)

        # Agrega la geometría simplificada al array de features
        feature = {
            "properties": {
                "id": cyclone_era5_node.id,
            },
            "geometry": mapping(rounded_wgs84_geom)
        }
        features.append(feature)

    # Formatear todos los registros como una colección de características
    geojson = {
        "type": "CycloneEra5NodeCollection",
        "features": features
    }
    
    return geojson