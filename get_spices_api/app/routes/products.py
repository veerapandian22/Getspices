from fastapi import APIRouter, Depends
from fastapi import Depends

router = APIRouter()


@router.get("/list")
async def list_product():
    return {'a': 'Cardamom'}

