from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create_sandwich(db: Session, sandwich):
    db_sandwich = models.Sandwich(
        customer_name=sandwich.customer_name,
        description=sandwich.description
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich


def get_sandwiches(db: Session):
    return db.query(models.Sandwich).all()


def get_one_sandwich(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()


def update(db: Session, sandwich_id, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    update_data = sandwich.dict(exclude_unset=True)
    db_sandwich.update(update_data, synchronize_session=False)
    db.commit()
    return db_sandwich.first()


def delete(db: Session, db_sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == db_sandwich)
    db_sandwich.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
