from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Menu(Base):
    __tablename__ = "menu"

    menuItem = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default="0.0")
    calories = Column(Integer, nullable=False, server_default="0")
    foodCategory = Column(String(20), nullable=False, server_default="food")