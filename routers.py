from typing import Annotated

from fastapi import APIRouter, HTTPException, Path

import schemas
import crud
from db.utils import db_dependency

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: db_dependency):
    db_product = crud.get_product_by_name(db=db, name=product.name)
    if db_product:
        raise HTTPException(
            status_code=400, detail="Product with this name already exists"
        )
    return crud.create_product(db=db, product=product)


@router.get("/", response_model=list[schemas.Product])
def get_products(
    db: db_dependency,
    page: Annotated[int, Path(ge=1)],
    per_page: Annotated[int, Path(ge=10, le=100)],
    product: str | None = None,
):
    return crud.get_products_list(
        db=db, per_page=per_page, page=page, product=product
    )


@router.get("/{product_id}/", response_model=schemas.Product)
def get_single_products(db: db_dependency, product_id: int):
    return crud.get_product_by_id(db=db, product_id=product_id)
