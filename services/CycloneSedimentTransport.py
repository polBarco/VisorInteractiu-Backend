from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.models import CycloneSedimentTransport
from utils.GeoJSONConverter import GeoJSONConverter

class CycloneSedimentTransportService:

    @staticmethod
    def get_all_cyclone_sediment_transport(db: Session):
        cyclone_sediment_transport_list = db.query(CycloneSedimentTransport).all()
        if not cyclone_sediment_transport_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cyclone sediment transport not found")
        else:
            return GeoJSONConverter.convert_to_geojson_list(
                cyclone_sediment_transport_list,
                "CycloneSedimentTransportCollection",
                lambda st: {
                    "id": st.id,
                    "transport": st.transport,
                    "percent": st.percent
                }
            )