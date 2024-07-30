from datetime import date
from typing import Optional
from pydantic import BaseModel


class PromotionsBase(BaseModel):
    promotionCode: int
    discount: float
    promotionExpiration: date


class PromotionsCreate(PromotionsBase):
    pass


class PromotionsUpdate(BaseModel):
    promotionCode: Optional[int] = None
    discount: Optional[float] = None
    promotionExpiration: Optional[date] = None


class Promotions(PromotionsBase):
    promotionCode: int

    class ConfigDict:
        from_attributes = True