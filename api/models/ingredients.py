from sqlalchemy import FLOAT, Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Ingredients(Base):
    __tablename__ = "ingredients"

    ingredientId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredientName = Column(String(100), unique=True, nullable=False)
    amountAvailable = Column(Integer, nullable=False)
    unit = Column(String(10), nullable=False, server_default="unit")