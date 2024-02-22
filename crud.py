from sqlalchemy import select
from sqlalchemy.orm import Session

import schemas
from db.models import DBProduct


def get_products_list(
    db: Session, per_page: int = 10, page: int = 1, product: str | None = None
):
    query = select(DBProduct)
    if product:
        query = query.where(DBProduct.name.icontains(product))
    query = query.limit(per_page).offset((page - 1) * per_page)
    return db.execute(query).scalars()


def get_product_by_name(db: Session, name: str):
    query = select(DBProduct).where(DBProduct.name == name)
    return db.execute(query).scalar()


def get_product_by_id(db: Session, product_id: int):
    query = select(DBProduct).where(DBProduct.id == product_id)
    return db.execute(query).scalar()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = DBProduct(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
