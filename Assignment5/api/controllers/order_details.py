from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create_order_detail(db: Session, order_detail):
    db_order_detail = models.OrderDetail(
        customer_name=order_detail.customer_name,
        description=order_detail.description
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail


def get_order_details(db: Session):
    return db.query(models.OrderDetail).all()


def get_one_order_detail(db: Session, order_detail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()


def update(db: Session, order_detail_id, order_detail):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    update_data = order_detail.dict(exclude_unset=True)
    db_order_detail.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_detail.first()


def delete(db: Session, db_order_detail):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == db_order_detail)
    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
