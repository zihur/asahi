from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.product import Product
from app.schemas.product import ProductRead, ProductSearchResponse

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/search", response_model=ProductSearchResponse)
def search_products(
    q: str = Query(..., min_length=1, description="型號或名稱關鍵字"),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    keyword = q.strip()
    pattern = f"%{keyword}%"

    stmt = (
        select(Product)
        .where(
            or_(
                Product.model_no.ilike(pattern),
                Product.name.ilike(pattern),
            )
        )
        .order_by(Product.model_no)
        .limit(limit)
    )
    items = db.scalars(stmt).all()

    count_stmt = select(func.count()).select_from(Product).where(
        or_(
            Product.model_no.ilike(pattern),
            Product.name.ilike(pattern),
        )
    )
    total = db.scalar(count_stmt) or 0

    return ProductSearchResponse(
        items=[ProductRead.model_validate(p) for p in items],
        total=total,
        q=keyword,
    )
