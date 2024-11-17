from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.rates.schemas import (
    RateDeleteResponse,
    RateResponse,
    RatesUpload,
    RatesUploadResponse,
)
from src.rates.services import (
    delete_rate_service,
    get_available_rates_service,
    upload_rates_service,
)
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


@router.get(
    path='/',
    summary='Получить список всех загруженных тарифов',
)
async def get_rates(
    cargo_type: Optional[str] = None,
    effective_date: Optional[datetime] = None,
    db_session: AsyncSession = Depends(get_session),
) -> List[RateResponse]:
    return await get_available_rates_service(
        session=db_session,
        cargo_type=cargo_type,
        effective_date=effective_date,
    )


@router.delete(
    path='/{rate_id}',
    summary='Удалить тариф по его ID',
)
async def delete_rate(
    rate_id: int,
    db_session: AsyncSession = Depends(get_session),
) -> RateDeleteResponse:
    await delete_rate_service(rate_id, db_session)
    return RateDeleteResponse
