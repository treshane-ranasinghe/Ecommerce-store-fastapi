# Ecommerce FastAPI Microservices

A fully containerized **E-commerce platform** built using **FastAPI microservices**, **PostgreSQL**, and **Docker Compose**. The project consists of three main services:

- **Product Service** – Manages products
- **Order Service** – Manages orders
- **Cart Service** – Manages user carts

Each service connects to its own PostgreSQL database, and all configurations are managed via a **global `.env` file**.

---

## Features

- Modular microservice architecture
- PostgreSQL databases for each service
- Dockerized services for easy deployment
- Environment configuration with `.env`
- SQLAlchemy ORM with Pydantic schemas
- Uvicorn for ASGI server with live reload
- Health checks for PostgreSQL before starting services

---

## Requirements

- Docker & Docker Compose
- Python 3.13+
- Git

---

## Project Structure

Ecommerce-fastapi/
├─ .env                        # Global environment variables for all services
├─ docker-compose.yml           # Docker Compose configuration for all services
├─ compose-init-sql/            # SQL scripts to initialize databases
│   ├─ 01_create_product_db.sql
│   ├─ 02_create_order_db.sql
│   └─ 03_create_cart_db.sql
├─ product_service/             # Product microservice
│   ├─ app/
│   │   ├─ main.py              # FastAPI app entrypoint
│   │   ├─ models/
│   │   │   └─ product.py       # SQLAlchemy models
│   │   ├─ schemas/
│   │   │   └─ product_schemas.py
│   │   ├─ db/
│   │   │   ├─ sessions.py      # SQLAlchemy session configuration
│   │   │   └─ config.py        # Pydantic settings
│   │   └─ routers/
│   │       └─ product_router.py
│   └─ requirements.txt
├─ order_service/               # Order microservice
│   ├─ app/
│   │   ├─ main.py
│   │   ├─ models/
│   │   ├─ schemas/
│   │   ├─ db/
│   │   │   ├─ sessions.py
│   │   │   └─ config.py
│   │   └─ routers/
│   └─ requirements.txt
├─ cart_service/                # Cart microservice
│   ├─ app/
│   │   ├─ main.py
│   │   ├─ models/
│   │   ├─ schemas/
│   │   ├─ db/
│   │   │   ├─ sessions.py
│   │   │   └─ config.py
│   │   └─ routers/
│   └─ requirements.txt
├─ README.md                    # Project documentation
└─ .gitignore                   # Git ignore file

