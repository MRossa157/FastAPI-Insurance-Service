from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.insurance.schemas import (
    InsuranceCalculateRequest,
    InsuranceCalculateResponse,
    InsuranceHistoryItem,
)
from src.insurance.services import (
    calculate_insurance_service,
    get_insurance_calculate_history_service,
)
from src.utils.database import get_session

router = APIRouter()


@router.post(
    path='/calculate',
    summary='Рассчитать стоимость страхования для груза',
)
async def calculate_insurance(
    insurance_data: InsuranceCalculateRequest,
    db_session: AsyncSession = Depends(get_session),
) -> InsuranceCalculateResponse:
    return InsuranceCalculateResponse(
        insurance_cost=await calculate_insurance_service(
            insurance_data=insurance_data,
            session=db_session,
        ),
    )


@router.get(
    path='/history',
    summary='Получить историю расчетов',
)
async def history_insurance(
    cargo_type: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db_session: AsyncSession = Depends(get_session),
) -> List[InsuranceHistoryItem]:
    return await get_insurance_calculate_history_service(
        cargo_type=cargo_type,
        start_date=start_date,
        end_date=end_date,
        session=db_session,
    )
