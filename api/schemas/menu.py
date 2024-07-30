from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MenuBase(BaseModel):
    dish: str
    price: float
    calories: int
    foodCategory: str


class MenuCreate(MenuBase):
    pass


class MenuUpdate(BaseModel):
    dish: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    foodCategory: Optional[str] = None


class Menu(MenuBase):
    menuItem: int

    class ConfigDict:
        from_attributes = True