from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.order import Order, OrderItem
from app.schemas.order_schema import OrderCreate, OrderOut

router = APIRouter(tags=["Orders"])

@router.post("/", response_model=OrderOut)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(
        user_id=order_data.user_id,
        total_amount=order_data.total_amount,
        status=order_data.status
    )
    db.add(new_order)
    db.flush()  # get order.id before adding items

    for item in order_data.items:
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(order_item)

    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/", response_model=list[OrderOut])
def get_all_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}/status")
def update_order_status(order_id: int, status: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = status
    db.commit()
    db.refresh(order)
    return {"message": f"Order status updated to {status}"}
