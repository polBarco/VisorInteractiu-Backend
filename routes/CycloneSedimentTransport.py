from fastapi import FastAPI, Depends, APIRouter
from core.database import get_db
from sqlalchemy.orm import Session
from services.CycloneSedimentTransport import CycloneSedimentTransportService

router = APIRouter(prefix="/api")
app = FastAPI()


@router.get("/cyclone_sediment_transport/all", tags=["cyclone sediment transport"])
async def get_all_cyclone_sediment_transpor(db: Session = Depends(get_db)):
    return CycloneSedimentTransportService.get_all_cyclone_sediment_transport(db)