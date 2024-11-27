from fastapi import FastAPI, Depends, APIRouter, Query
from core.database import get_db
from sqlalchemy.orm import Session
from services.d50 import d50Service

router = APIRouter(prefix="/api")
app = FastAPI()


@router.get("/d50", tags=["d50"])
async def get_d50_by_name(name: str = Query(...), db: Session = Depends(get_db)):
    return d50Service.get_d50_by_name(name, db)
