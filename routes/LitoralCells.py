from fastapi import FastAPI, Depends, APIRouter, Query
from core.database import get_db
from sqlalchemy.orm import Session
from services.LitoralCells import LitoralCellsService

router = APIRouter(prefix="/api")
app = FastAPI()

@router.get("/litoral_cells", tags=["litoral cells"])
async def get_litoral_cells_by_name(name: str = Query(...), db: Session = Depends(get_db)):
    return LitoralCellsService.get_litoral_cells_by_name(name, db)