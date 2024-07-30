from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    DATETIME,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Reviews(Base):
    __tablename__ = "reviews"

    reviewId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reviewText = Column(String(200))
    reviewScore = Column(Integer)
    menuItem = Column(Integer, ForeignKey("menu.menuItem"))
    reviewDate = Column(DATETIME, nullable=False, default=datetime.now)

    menu = relationship("Menu", backref="reviews")