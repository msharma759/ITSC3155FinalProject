# controllers/reviews_controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import Reviews
from ..schemas import ReviewCreate, ReviewUpdate

def get_review(db: Session, review_id: int):
    return db.query(Reviews).filter(Reviews.reviewId == review_id).first()

def get_reviews(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reviews).offset(skip).limit(limit).all()

def create_review(db: Session, review: ReviewCreate):
    db_review = Reviews(
        reviewText=review.reviewText,
        reviewScore=review.reviewScore,
        menuItem=review.menuItem,
        reviewDate=review.reviewDate or datetime.now()
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_review(db: Session, review_id: int, review: ReviewUpdate):
    db_review = get_review(db, review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    for key, value in review.dict(exclude_unset=True).items():
        setattr(db_review, key, value)
    db.commit()
    db.refresh(db_review)
    return db_review

def delete_review(db: Session, review_id: int):
    db_review = get_review(db, review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    db.delete(db_review)
    db.commit()
    return db_review
