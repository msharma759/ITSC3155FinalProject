# routers/resource.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..controllers import resource_controller
from ..schemas import Resource, ResourceCreate, ResourceUpdate

router = APIRouter(
    prefix="/resources",
    tags=["resources"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Resource])
def read_resources(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    resources = resource_controller.get_resources(db, skip=skip, limit=limit)
    return resources

@router.get("/{resource_id}", response_model=Resource)
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    db_resource = resource_controller.get_resource(db, resource_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return db_resource

@router.post("/", response_model=Resource)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    return resource_controller.create_resource(db, resource)

@router.put("/{resource_id}", response_model=Resource)
def update_resource(resource_id: int, resource: ResourceUpdate, db: Session = Depends(get_db)):
    return resource_controller.update_resource(db, resource_id, resource)

@router.delete("/{resource_id}", response_model=Resource)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resource_controller.delete_resource(db, resource_id)
