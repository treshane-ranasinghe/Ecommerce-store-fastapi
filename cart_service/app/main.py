from fastapi import FastAPI
from app.db.session import engine, Base
from app.db import base  # Import models to register with Base
from app.routers import cart_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cart Service")

app.include_router(cart_router.router)
