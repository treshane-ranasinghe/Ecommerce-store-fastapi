from pydantic import BaseModel

class CartBase(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float
    user_id: int

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int

    class Config:
        orm_mode = True
