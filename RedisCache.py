from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import json
from typing import Optional

router = APIRouter()

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)

class ProductSchema(BaseModel):
    id: int
    name: str
    price: int
    description: str
    class Config:
        from_attributes = True

class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None

redis_url = ""

from redis.asyncio import Redis
redis_client = Redis.from_url(redis_url, decode_responses=True)
@router.get("/products/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await redis_client.get(f"product:{product_id}")
    if not result:
        db_result = await db.execute(select(Product).where(Product.id == product_id))
        product = db_result.scalar_one_or_none()
        if not product:
                raise HTTPException(status_code=404, detail="Product not found")
        product_data = ProductSchema.model_validate(product).model_dump()
        await redis_client.setex(f"product:{product_id}", 3600, json.dumps(product_data))
        return product
    product = json.loads(result)
    return product


@router.put("/products/{product_id}", response_model=ProductSchema)
async def update_product(product_id:int, product_data: ProductUpdateSchema, db: AsyncSession = Depends(get_db)):
    db_result = await db.execute(select(Product).where(Product.id == product_id))
    product = db_result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    update_data = product_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(product, key, value)
    await db.commit()
    await db.refresh(product)
    await redis_client.delete(f"product:{product_id}")
    return product