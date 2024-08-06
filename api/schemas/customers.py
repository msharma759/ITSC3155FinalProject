from typing import Optional, List
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class Order(BaseModel):
    id: int
    description: str
    customer_id: int

class Customer(CustomerBase):
    id: int
    orders: Optional[List[Order]] = []

    class Config:
        orm_mode = True

# Resolve forward references
Customer.update_forward_refs()
Order.update_forward_refs()
