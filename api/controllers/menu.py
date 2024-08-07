# controllers/menu_controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import Menu
from ..schemas import MenuCreate, MenuUpdate

def get_menu_item(db: Session, menu_item_id: int):
    return db.query(Menu).filter(Menu.menuItem == menu_item_id).first()

def get_menu(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Menu).offset(skip).limit(limit).all()

def create_menu_item(db: Session, menu_item: MenuCreate):
    db_menu_item = Menu(
        dish=menu_item.dish,
        price=menu_item.price,
        calories=menu_item.calories,
        foodCategory=menu_item.foodCategory
    )
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

def update_menu_item(db: Session, menu_item_id: int, menu_item: MenuUpdate):
    db_menu_item = get_menu_item(db, menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    for key, value in menu_item.dict(exclude_unset=True).items():
        setattr(db_menu_item, key, value)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

def delete_menu_item(db: Session, menu_item_id: int):
    db_menu_item = get_menu_item(db, menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    db.delete(db_menu_item)
    db.commit()
    return db_menu_item
