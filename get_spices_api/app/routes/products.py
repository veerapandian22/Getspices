from fastapi import APIRouter, Depends
from fastapi import Depends
from ..db import database, product_table

router = APIRouter()


@router.get("/list")
async def list_product():
    product_query = product_table.select()    
    return await database.fetch_all(product_query)

