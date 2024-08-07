# routers/sandwich.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..controllers import sandwich_controller
from ..schemas import Sandwich, SandwichCreate, SandwichUpdate

router = APIRouter(
    prefix="/sandwiches",
    tags=["sandwiches"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Sandwich])
def read_sandwiches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sandwiches = sandwich_controller.get_sandwiches(db, skip=skip, limit=limit)
    return sandwiches

@router.get("/{sandwich_id}", response_model=Sandwich)
def read_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = sandwich_controller.get_sandwich(db, sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return db_sandwich

@router.post("/", response_model=Sandwich)
def create_sandwich(sandwich: SandwichCreate, db: Session = Depends(get_db)):
    return sandwich_controller.create_sandwich(db, sandwich)

@router.put("/{sandwich_id}", response_model=Sandwich)
def update_sandwich(sandwich_id: int, sandwich: SandwichUpdate, db: Session = Depends(get_db)):
    return sandwich_controller.update_sandwich(db, sandwich_id, sandwich)

@router.delete("/{sandwich_id}", response_model=Sandwich)
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return sandwich_controller.delete_sandwich(db, sandwich_id)
