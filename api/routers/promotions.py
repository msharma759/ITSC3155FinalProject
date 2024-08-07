# routers/promotions.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..controllers import promotions_controller
from ..schemas import Promotions, PromotionsCreate, PromotionsUpdate

router = APIRouter(
    prefix="/promotions",
    tags=["promotions"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Promotions])
def read_promotions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    promotions = promotions_controller.get_promotions(db, skip=skip, limit=limit)
    return promotions

@router.get("/{promotion_code}", response_model=Promotions)
def read_promotion(promotion_code: int, db: Session = Depends(get_db)):
    db_promotion = promotions_controller.get_promotion(db, promotion_code)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return db_promotion

@router.post("/", response_model=Promotions)
def create_promotion(promotion: PromotionsCreate, db: Session = Depends(get_db)):
    return promotions_controller.create_promotion(db, promotion)

@router.put("/{promotion_code}", response_model=Promotions)
def update_promotion(promotion_code: int, promotion: PromotionsUpdate, db: Session = Depends(get_db)):
    return promotions_controller.update_promotion(db, promotion_code, promotion)

@router.delete("/{promotion_code}", response_model=Promotions)
def delete_promotion(promotion_code: int, db: Session = Depends(get_db)):
    return promotions_controller.delete_promotion(db, promotion_code)
