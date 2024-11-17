from datetime import datetime
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.rates.crud import add_rates, get_rates
from src.rates.schemas import RateResponse, RatesUpload
from src.utils.models.models import Rates


async def upload_rates_service(
    data: RatesUpload,
    session: AsyncSession,
) -> None:
    rates = []
    for date, rates_info in data.root.items():
        rates = [
            Rates(date=date, cargo_type=rate.cargo_type, rate=rate.rate)
            for rate in rates_info
        ]

    await add_rates(rates, session)


async def get_available_rates_service(
    session: AsyncSession,
    cargo_type: Optional[str],
    effective_date: Optional[datetime],
) -> List[RateResponse]:
    rates = await get_rates(
        session=session,
        cargo_type=cargo_type,
        effective_date=effective_date,
    )

    return [
        RateResponse(
            cargo_type=rate.cargo_type,
            rate=rate.rate,
            effective_date=rate.date,
        )
        for rate in rates
    ]
