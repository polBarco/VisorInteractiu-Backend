from fastapi import FastAPI, Depends, APIRouter, HTTPException
from core.database import get_db
from sqlalchemy.orm import Session
from services.Cartography import CartographyService
from schemas.Cartography import CartographyBase

router = APIRouter(prefix="/api")
app = FastAPI()

@router.get("/cartography/{gid}", tags=["cartography"])
async def get_cartography(gid: int, db: Session = Depends(get_db)):
    return CartographyService.get_cartography(gid, db)
    

