from fastapi import APIRouter, Depends
from fastapi import Depends

router = APIRouter()


@router.post("/create")
async def create_order():
    """
    TODO: Add to card
    """
    return {"Response": "Your order placed successfully"}


@router.get("/create/<orderId>")
async def order_detail(orderId: int):
    """
    TODO: Add to card
    """
    return {"Response": f"Details for your order: {orderId}"}