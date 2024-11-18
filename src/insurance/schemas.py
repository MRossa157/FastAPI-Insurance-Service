from datetime import datetime

from pydantic import BaseModel, Field


class InsuranceCalculateRequest(BaseModel):
    cargo_type: str = Field(..., description='Тип груза', example='electronics')
    declared_value: float = Field(
        ...,
        description='Объявленная стоимость груза',
        example=10000,
    )
    date: datetime = Field(..., description='Дата', example='2024-02-01')


class InsuranceCalculateResponse(BaseModel):
    insurance_cost: float = Field(
        ...,
        description='Стоимость страховки',
        example=1000,
    )


class InsuranceHistoryItem(BaseModel):
    cargo_type: str = Field(..., description='Тип груза', example='electronics')
    declared_value: float = Field(
        ...,
        description='Объявленная стоимость груза',
        example=10000,
    )
    insurance_cost: float = Field(
        ...,
        description='Стоимость страховки',
        example=1000,
    )
    date: datetime = Field(..., description='Дата', example='2024-02-01')