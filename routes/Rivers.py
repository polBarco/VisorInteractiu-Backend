from fastapi import FastAPI, Depends, APIRouter, Query
from core.database import get_db
from sqlalchemy.orm import Session
from services.Rivers import RiversService

router = APIRouter(prefix="/api")
app = FastAPI()

@router.get("/rivers", tags=["rivers"])
async def get_all_rivers(db: Session = Depends(get_db)):
    return RiversService.get_all_rivers(db)