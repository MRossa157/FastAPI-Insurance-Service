from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.rates.schemas import (
    RateResponse,
    RatesUpload,
    RatesUploadResponse,
)
from src.rates.services import get_available_rates_service, upload_rates_service
from src.utils.database import get_session

router = APIRouter()


@router.post(
    path='/upload',
    summary='Загрузить информацию о тарифах',
)
async def upload_rates(
    rates_info: RatesUpload,
    db_session: AsyncSession = Depends(get_session),
) -> RatesUploadResponse:
    await upload_rates_service(rates_info, db_session)
    return RatesUploadResponse


@router.get('/')
async def get_rates(
    db_session: AsyncSession = Depends(get_session),
    cargo_type: Optional[str] = None,
    effective_date: Optional[datetime] = None,
) -> List[RateResponse]:
    return await get_available_rates_service(
        session=db_session,
        cargo_type=cargo_type,
        effective_date=effective_date,
    )
