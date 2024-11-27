from pyproj import Transformer
from geoalchemy2.shape import to_shape
from shapely.ops import transform
from shapely.geometry import mapping

class GeoJSONConverter:

    @staticmethod
    def convert_to_geojson_list(objects_list: list, collection_type: str, properties_func, simplify_tolerance: float = None) -> dict:
        transformer = Transformer.from_crs("EPSG:32736", "EPSG:4326", always_xy=True)
        features = []

        for obj in objects_list:
            geom = to_shape(obj.geom)
            wgs84_geom = transform(transformer.transform, geom)

            if simplify_tolerance is not None:
                wgs84_geom = wgs84_geom.simplify(simplify_tolerance, preserve_topology=True)

            feature = {
                "properties": properties_func(obj),
                "geometry": mapping(wgs84_geom)
            }
            features.append(feature)

        return {
            "type": collection_type,
            "features": features
        }
