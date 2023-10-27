from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create_orderdetail(db: Session, orderdetail):
    db_orderdetail = models.OrderDetail(
        customer_name=orderdetail.customer_name,
        description=orderdetail.description
    )
    db.add(db_orderdetail)
    db.commit()
    db.refresh(db_orderdetail)
    return db_orderdetail


def get_orderdetails(db: Session):
    return db.query(models.OrderDetail).all()


def get_one_orderdetail(db: Session, orderdetail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == orderdetail_id).first()


def update(db: Session, orderdetail_id, orderdetail):
    db_orderdetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == orderdetail_id)
    update_data = orderdetail.dict(exclude_unset=True)
    db_orderdetail.update(update_data, synchronize_session=False)
    db.commit()
    return db_orderdetail.first()


def delete(db: Session, db_orderdetail):
    db_orderdetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == db_orderdetail)
    db_orderdetail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
