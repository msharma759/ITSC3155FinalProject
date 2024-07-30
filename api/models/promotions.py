from sqlalchemy import FLOAT, Column, ForeignKey, Integer, String, DECIMAL, DATE
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotions(Base):
    __tablename__ = "promotions"

    promotionCode = Column(Integer, primary_key=True)
    promotionExpiration = Column(DATE, nullable=False)
    discount = Column(DECIMAL(4, 2), nullable=False, server_default="0.0")