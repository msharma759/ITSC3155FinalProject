# controllers/ingredients_controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import Ingredients
from ..schemas import IngredientsCreate, IngredientsUpdate

def get_ingredient(db: Session, ingredient_id: int):
    return db.query(Ingredients).filter(Ingredients.ingredientId == ingredient_id).first()

def get_ingredients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ingredients).offset(skip).limit(limit).all()

def create_ingredient(db: Session, ingredient: IngredientsCreate):
    db_ingredient = Ingredients(
        ingredientName=ingredient.ingredientName,
        amountAvailable=ingredient.amountAvailable,
        unit=ingredient.unit
    )
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

def update_ingredient(db: Session, ingredient_id: int, ingredient: IngredientsUpdate):
    db_ingredient = get_ingredient(db, ingredient_id)
    if db_ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    for key, value in ingredient.dict(exclude_unset=True).items():
        setattr(db_ingredient, key, value)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

def delete_ingredient(db: Session, ingredient_id: int):
    db_ingredient = get_ingredient(db, ingredient_id)
    if db_ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    db.delete(db_ingredient)
    db.commit()
    return db_ingredient
