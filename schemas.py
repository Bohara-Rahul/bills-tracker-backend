from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class BillBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    amount: int = Field()
    description: str = Field(min_length=1)
    reference: str = Field(min_length=1)
    date_paid: str = Field(min_length=1, max_length=20)


class BillCreate(BillBase):
    pass


class BillResponse(BillBase):
    pass