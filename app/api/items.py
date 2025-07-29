from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services import item as item_service

router = APIRouter()


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, owner_id: int, db: Session = Depends(get_db)):
    """Create a new item"""
    return item_service.create_item(db=db, item=item, owner_id=owner_id)


@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get list of items"""
    items = item_service.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/user/{owner_id}", response_model=List[Item])
def read_items_by_owner(owner_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get items by owner"""
    items = item_service.get_items_by_owner(db, owner_id=owner_id, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Get item by ID"""
    db_item = item_service.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemUpdate, db: Session = Depends(get_db)):
    """Update item"""
    db_item = item_service.update_item(db, item_id=item_id, item_update=item_update)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete item"""
    success = item_service.delete_item(db, item_id=item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")