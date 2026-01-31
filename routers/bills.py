from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models
from database import get_db
from schemas import BillCreate, BillResponse

router = APIRouter()

@router.get("", response_model=list[BillResponse])
async def get_bills(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Bill)
        .order_by(models.Bill.date_paid.desc())
    )
    bills = result.scalars().all()
    return bills


@router.post("", response_model=BillResponse, status_code=status.HTTP_201_CREATED)
async def create_bill(payload: BillCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    new_bill = models.Bill(
        title=payload.title,
        amount=payload.amount,
        description=payload.description,
        reference=payload.reference,
        date_paid=payload.date_paid,
    )
    db.add(new_bill)
    await db.commit()
    await db.refresh(new_bill)
    return new_bill