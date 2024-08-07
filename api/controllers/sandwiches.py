# controllers/sandwich_controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import Sandwich
from ..schemas import SandwichCreate, SandwichUpdate

def get_sandwich(db: Session, sandwich_id: int):
    return db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()

def get_sandwiches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sandwich).offset(skip).limit(limit).all()

def create_sandwich(db: Session, sandwich: SandwichCreate):
    db_sandwich = Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price,
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def update_sandwich(db: Session, sandwich_id: int, sandwich: SandwichUpdate):
    db_sandwich = get_sandwich(db, sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    for key, value in sandwich.dict(exclude_unset=True).items():
        setattr(db_sandwich, key, value)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = get_sandwich(db, sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    db.delete(db_sandwich)
    db.commit()
    return db_sandwich
