from typing import List, Optional
from pydantic import BaseModel


"""
Para evitar confusão entre os modelos SQLAlchemy e os modelos Pydantic , teremos o arquivo models.pycom os modelos SQLAlchemy e o arquivo schemas.pycom os modelos Pydantic.
Esses modelos Pydantic definem mais ou menos um "esquema" (uma forma de dados válida).
Portanto, isso nos ajudará a evitar confusão ao usar os dois.
"""


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
