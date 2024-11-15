from fastapi import FastAPI, Depends, APIRouter
from core.database import get_db
from sqlalchemy.orm import Session
from services.CycloneEra5Node import CycloneEra5NodeService

router = APIRouter(prefix="/api")
app = FastAPI()

@router.get("/cyclone_era5_node/all", tags=["cyclone era5 node"])
async def get_all_cyclone_era5_node(db: Session = Depends(get_db)):
    return CycloneEra5NodeService.get_all_cyclone_era5_node(db)