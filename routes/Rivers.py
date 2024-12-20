from fastapi import FastAPI, Depends, APIRouter, Query
from core.database import get_db
from sqlalchemy.orm import Session
from services.Rivers import RiversService

router = APIRouter(prefix="/api")
app = FastAPI()

@router.get("/rivers", tags=["rivers"])
async def get_paginated_rivers(
    page: int = Query(1, ge=1, description="Page number (starts at 1)"),
    limit: int = Query(2500, ge=1, le=2500, description="Elementos por página"),
    db: Session = Depends(get_db)
):
    """
    Endpoint to get rivers with pagination.
    """
    rivers_geojson, total = RiversService.get_paginated_rivers(page=page, limit=limit, db=db)
    total_pages = (total // limit) + (1 if total % limit != 0 else 0)

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages,
        "data": rivers_geojson
    }
