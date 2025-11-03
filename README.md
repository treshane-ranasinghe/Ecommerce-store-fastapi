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

