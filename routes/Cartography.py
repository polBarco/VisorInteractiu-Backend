from fastapi import FastAPI, Depends, APIRouter, Query
from core.database import get_db
from sqlalchemy.orm import Session
from services.Cartography import CartographyService

router = APIRouter(prefix="/api")
app = FastAPI()


@router.get("/cartography", tags=["cartography"])
async def get_cartography_by_element(element: str = Query(...), db: Session = Depends(get_db)):
    return CartographyService.get_cartography_by_element(element, db)
    

