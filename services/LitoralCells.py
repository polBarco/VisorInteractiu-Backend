from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import LitoralCells
from pyproj import Transformer
from geoalchemy2.shape import to_shape
from shapely.ops import transform
from shapely.geometry import mapping

class LitoralCellsService:

    @staticmethod
    def get_litoral_cells_by_name(name: str, db: Session):
        litoral_cells_list = db.query(LitoralCells).filter(LitoralCells.name == name).all()
        if not litoral_cells_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="LitoralCells not found")
        else:
            return convert_to_geojson_list(litoral_cells_list)
        
def round_coordinates(geometry, precision=5):
    """Función para redondear las coordenadas de una geometría."""
    def rounder(x, y, z=None):
        return (round(x, precision), round(y, precision)) if z is None else (round(x, precision), round(y, precision), round(z, precision))
    
    return transform(rounder, geometry)

def convert_to_geojson_list(litoral_cells_list: list) -> dict:
    # Configura el transformador UTM a WGS84
    transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)

    features = []

    for litoral_cells in litoral_cells_list:
        # Convierte la geometría a un objeto Shapely
        geom = to_shape(litoral_cells.geom)

        # Convierte las coordenadas de UTM a WGS84 después de simplificar
        wgs84_geom = transform(transformer.transform, geom)
        # rounded_wgs84_geom = round_coordinates(wgs84_geom, precision=6)

        # simplified_geom = rounded_wgs84_geom.simplify(0.001, preserve_topology=True)

        # Agrega la geometría simplificada al array de features
        feature = {
            "properties": {
                "name": litoral_cells.name,
                "length": litoral_cells.length,
                "length_km": litoral_cells.length_km,
                "coord_xfin": litoral_cells.coord_xfin,
                "coord_yfin": litoral_cells.coord_yfin,
                "coord_yini": litoral_cells.coord_yini,
                "coord_xini": litoral_cells.coord_xini,
                "par_impar": litoral_cells.par_impar
            },
            "geometry": mapping(wgs84_geom)
        }
        features.append(feature)

    # Formatear todos los registros como una colección de características
    geojson = {
        "type": "LitoralCellsCollection",
        "features": features
    }
    
    return geojson