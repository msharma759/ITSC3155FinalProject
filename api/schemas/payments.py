from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    card_information: str
    transaction_status: str
    payment_type: str
    order_id: int

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    card_information: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None
    order_id: Optional[int] = None

class Payment(PaymentBase):
    id: int
    order: Optional['Order'] = None

    class Config:
        orm_mode = True
