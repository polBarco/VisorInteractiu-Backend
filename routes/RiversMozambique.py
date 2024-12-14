from fastapi import FastAPI, Depends, APIRouter, Query
from core.database import get_db
from sqlalchemy.orm import Session
from services.RiversMozambique import RiversMozambiqueService

router = APIRouter(prefix="/api")
app = FastAPI()

@router.get("/rivers_mozambique", tags=["rivers_mozambique"])
async def get_rivers_by_region(region: str = Query(...), db: Session = Depends(get_db)):
    return RiversMozambiqueService.get_rivers_by_region(region, db)