from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    order_date: Optional[datetime] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None
    customer_id: Optional[int] = None
class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    customer: Optional['Customer'] = None
    payment: Optional['Payment'] = None
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
