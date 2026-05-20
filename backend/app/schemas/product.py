from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    model_no: str
    name: str
    brand: str | None = None
    spec: str | None = None
    remark: str | None = None
    created_at: datetime
    updated_at: datetime


class ProductSearchResponse(BaseModel):
    items: list[ProductRead]
    total: int
    q: str
