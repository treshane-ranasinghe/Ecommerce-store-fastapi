from fastapi import FastAPI
from app.db.session import Base, engine
from app.routers import product_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Service")
app.include_router(product_router.router, prefix="/products")
