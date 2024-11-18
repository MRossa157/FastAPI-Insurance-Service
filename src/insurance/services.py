from datetime import datetime
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.constants import NUMBER_PRECISION
from src.insurance.exceptions import ApplicableRateNotFoundError
from src.insurance.schemas import InsuranceCalculateRequest
from src.rates.schemas import RateResponse
from src.rates.services import get_available_rates_service


async def calculate_insurance_service(
    session: AsyncSession,
    insurance_data: InsuranceCalculateRequest,
) -> float:
    cargo_tariffs = await get_available_rates_service(
        session=session,
        cargo_type=insurance_data.cargo_type,
    )

    applicable_rate = find_applicable_rate(
        rates=cargo_tariffs,
        insurance_date=insurance_data.date,
    )
    if applicable_rate is None:
        raise ApplicableRateNotFoundError(
            cargo_type=insurance_data.cargo_type,
            date=insurance_data.date,
        )

    insurance_cost = round(
        insurance_data.declared_value * applicable_rate.rate,
        NUMBER_PRECISION,
    )

    #TODO добавить запись в БД

    return insurance_cost


def find_applicable_rate(
    rates: List[RateResponse],
    insurance_date: datetime,
) -> Optional[RateResponse]:
    applicable_rates = [
        rate for rate in rates if rate.effective_date <= insurance_date
    ]

    if applicable_rates:
        return max(applicable_rates, key=lambda rate: rate.effective_date)

    return None
