from fastapi import FastAPI
from app.db.session import Base, engine
from app.routers import order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Service API")

app.include_router(order_router.router, prefix="/orders")

@app.get("/")
def root():
    return {"message": "Order Service is running!"}
