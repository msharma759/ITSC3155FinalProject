# controllers/promotions_controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import Promotions
from ..schemas import PromotionsCreate, PromotionsUpdate

def get_promotion(db: Session, promotion_code: int):
    return db.query(Promotions).filter(Promotions.promotionCode == promotion_code).first()

def get_promotions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Promotions).offset(skip).limit(limit).all()

def create_promotion(db: Session, promotion: PromotionsCreate):
    db_promotion = Promotions(
        promotionCode=promotion.promotionCode,
        promotionExpiration=promotion.promotionExpiration,
        discount=promotion.discount
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def update_promotion(db: Session, promotion_code: int, promotion: PromotionsUpdate):
    db_promotion = get_promotion(db, promotion_code)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    for key, value in promotion.dict(exclude_unset=True).items():
        setattr(db_promotion, key, value)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def delete_promotion(db: Session, promotion_code: int):
    db_promotion = get_promotion(db, promotion_code)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    db.delete(db_promotion)
    db.commit()
    return db_promotion
