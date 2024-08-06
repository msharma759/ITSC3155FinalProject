from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=True)
    address = Column(String(300), nullable=True)

    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(300), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship("Customer", back_populates="orders")
