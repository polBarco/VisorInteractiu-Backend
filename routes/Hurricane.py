from fastapi import FastAPI, APIRouter, Depends, Query
from core.database import get_db
from sqlalchemy.orm import Session
from services.Hurricane import HurricaneService

router = APIRouter(prefix="/api")
app = FastAPI()


@router.get("/hurricane/types", tags=["hurricane"])
async def get_hurricane_types(db: Session = Depends(get_db)):
    return HurricaneService.get_hurricane_types(db)

@router.get("/hurricane/years/{type}", tags=["hurricane"])
async def get_hurricane_years_by_type(type: str, db: Session = Depends(get_db)):
    return HurricaneService.get_hurricane_years_by_type(type, db)

@router.get("/hurricane/{type}/{year}", tags=["hurricane"])
async def get_hurricane_by_type_and_year(type: str, year: int, db: Session = Depends(get_db)):
    return HurricaneService.get_hurricane_by_type_and_year(type, year, db)
