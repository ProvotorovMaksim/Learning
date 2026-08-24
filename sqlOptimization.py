from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from pydantic import BaseModel

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Связь с заказами
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Integer)
    user = relationship("User", back_populates="orders")

class OrderSchema(BaseModel):
    id: int
    user_id: int
    total_amount: int
    class Config:
            from_attributes = True

class UserSchema(BaseModel):
    id: int
    name: str
    orders: list[OrderSchema]
    class Config:
            from_attributes = True

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

router = APIRouter()

# Предположим, get_db - это зависимость, отдающая асинхронную сессию
@router.get("/users-with-orders")
async def get_users_with_orders(db: AsyncSession = Depends(get_db)):
    # 1. Получаем всех пользователей (1 запрос)
    result = await db.execute(select(User).options(selectinload(User.orders)))
    user = result.scalars().all()
    return user
