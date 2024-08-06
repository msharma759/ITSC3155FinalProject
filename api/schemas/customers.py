from pydantic import BaseModel
from typing import Optional, List

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

class Customer(CustomerBase):
    id: int
    orders: Optional[List['Order']] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

