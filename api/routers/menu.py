# routers/menu.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..controllers import menu_controller
from ..schemas import Menu, MenuCreate, MenuUpdate

router = APIRouter(
    prefix="/menu",
    tags=["menu"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Menu])
def read_menu(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    menu = menu_controller.get_menu(db, skip=skip, limit=limit)
    return menu

@router.get("/{menu_item_id}", response_model=Menu)
def read_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    db_menu_item = menu_controller.get_menu_item(db, menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_menu_item

@router.post("/", response_model=Menu)
def create_menu_item(menu_item: MenuCreate, db: Session = Depends(get_db)):
    return menu_controller.create_menu_item(db, menu_item)

@router.put("/{menu_item_id}", response_model=Menu)
def update_menu_item(menu_item_id: int, menu_item: MenuUpdate, db: Session = Depends(get_db)):
    return menu_controller.update_menu_item(db, menu_item_id, menu_item)

@router.delete("/{menu_item_id}", response_model=Menu)
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return menu_controller.delete_menu_item(db, menu_item_id)
