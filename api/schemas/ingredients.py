# from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class IngredientsBase(BaseModel):
    amountAvailable: int
    ingredientName: str
    unit: str


class IngredientsCreate(IngredientsBase):
    pass


class IngredientsUpdate(BaseModel):
    amountAvailable: Optional[int] = None
    ingredientName: Optional[str] = None
    unit: Optional[str] = None


class Ingredients(IngredientsBase):
    ingredientId: int

    class ConfigDict:
        from_attributes = True