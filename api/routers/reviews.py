# routers/reviews.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..controllers import reviews_controller
from ..schemas import Review, ReviewCreate, ReviewUpdate

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Review])
def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reviews = reviews_controller.get_reviews(db, skip=skip, limit=limit)
    return reviews

@router.get("/{review_id}", response_model=Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    db_review = reviews_controller.get_review(db, review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return reviews_controller.create_review(db, review)

@router.put("/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewUpdate, db: Session = Depends(get_db)):
    return reviews_controller.update_review(db, review_id, review)

@router.delete("/{review_id}", response_model=Review)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return reviews_controller.delete_review(db, review_id)
