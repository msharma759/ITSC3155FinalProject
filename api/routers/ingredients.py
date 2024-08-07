# routers/ingredients.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..controllers import ingredients_controller
from ..schemas import Ingredients, IngredientsCreate, IngredientsUpdate

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Ingredients])
def read_ingredients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ingredients = ingredients_controller.get_ingredients(db, skip=skip, limit=limit)
    return ingredients

@router.get("/{ingredient_id}", response_model=Ingredients)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    db_ingredient = ingredients_controller.get_ingredient(db, ingredient_id)
    if db_ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return db_ingredient

@router.post("/", response_model=Ingredients)
def create_ingredient(ingredient: IngredientsCreate, db: Session = Depends(get_db)):
    return ingredients_controller.create_ingredient(db, ingredient)

@router.put("/{ingredient_id}", response_model=Ingredients)
def update_ingredient(ingredient_id: int, ingredient: IngredientsUpdate, db: Session = Depends(get_db)):
    return ingredients_controller.update_ingredient(db, ingredient_id, ingredient)

@router.delete("/{ingredient_id}", response_model=Ingredients)
def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    return ingredients_controller.delete_ingredient(db, ingredient_id)
