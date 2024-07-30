from datetime import datetime
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from .menu import Menu


class ReviewsBase(BaseModel):
    reviewText: str
    reviewScore: int = Field(..., ge=0, le=10, description="Must be between 0 and 10")


class ReviewsCreate(ReviewsBase):
    menuItem: int


class ReviewsUpdate(BaseModel):
    reviewText: Optional[str] = None
    reviewScore: Optional[int] = Field(
        ..., ge=0, le=10, description="Must be between 0 and 10"
    )
    menuItem: Optional[int] = None


class Reviews(ReviewsBase):
    reviewId: int
    reviewDate: datetime
    menu: Menu

    class ConfigDict:
        from_attributes = True