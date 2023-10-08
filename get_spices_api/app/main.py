from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import products, order
# from app.db import database

app = FastAPI()

# origins = [
#     settings.CLIENT_ORIGIN,
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(products.router, tags=['Products'], prefix='/api/products')
app.include_router(order.router, tags=['Order'], prefix='/api/order')

# @app.on_event("startup")
# async def startup():
#     await database.connect()

@app.get('/api/healthchecker')
def root():
    return {'message': 'Welcome to GetSpices API'}