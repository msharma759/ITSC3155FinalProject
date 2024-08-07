# routers/recipe.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..controllers import recipe_controller
from ..schemas import Recipe, RecipeCreate, RecipeUpdate

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Recipe])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    recipes = recipe_controller.get_recipes(db, skip=skip, limit=limit)
    return recipes

@router.get("/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = recipe_controller.get_recipe(db, recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@router.post("/", response_model=Recipe)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    return recipe_controller.create_recipe(db, recipe)

@router.put("/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db)):
    return recipe_controller.update_recipe(db, recipe_id, recipe)

@router.delete("/{recipe_id}", response_model=Recipe)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipe_controller.delete_recipe(db, recipe_id)
