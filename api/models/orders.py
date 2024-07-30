from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    tracking_number = Column(String(50), unique=True, nullable=True)
    order_status = Column(String(50), nullable=True)
    total_price = Column(DECIMAL(10, 2), nullable=False)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    customer = relationship("Customer", back_populates="orders")
    payment = relationship("Payment", back_populates="order", uselist=False)
    order_details = relationship("OrderDetail", back_populates="order")