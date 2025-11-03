from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.cart import Cart as CartModel
from app.schemas.cart_schema import CartCreate, Cart

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

# Create a new cart item
@router.post("/", response_model=Cart)
def create_cart(cart: CartCreate, db: Session = Depends(get_db)):
    db_cart = CartModel(**cart.dict())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

# Get all cart items for a user
@router.get("/user/{user_id}", response_model=list[Cart])
def get_cart_items(user_id: int, db: Session = Depends(get_db)):
    items = db.query(CartModel).filter(CartModel.user_id == user_id).all()
    return items

# Delete a cart item
@router.delete("/{cart_id}")
def delete_cart_item(cart_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(CartModel).filter(CartModel.id == cart_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(cart_item)
    db.commit()
    return {"detail": "Cart item deleted successfully"}
