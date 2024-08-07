# controllers/resource_controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import Resource
from ..schemas import ResourceCreate, ResourceUpdate

def get_resource(db: Session, resource_id: int):
    return db.query(Resource).filter(Resource.id == resource_id).first()

def get_resources(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Resource).offset(skip).limit(limit).all()

def create_resource(db: Session, resource: ResourceCreate):
    db_resource = Resource(
        item=resource.item,
        amount=resource.amount,
        unit=resource.unit
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def update_resource(db: Session, resource_id: int, resource: ResourceUpdate):
    db_resource = get_resource(db, resource_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    for key, value in resource.dict(exclude_unset=True).items():
        setattr(db_resource, key, value)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def delete_resource(db: Session, resource_id: int):
    db_resource = get_resource(db, resource_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(db_resource)
    db.commit()
    return db_resource
