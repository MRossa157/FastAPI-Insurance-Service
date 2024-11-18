from datetime import datetime
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.constants import NUMBER_PRECISION
from src.insurance.crud import (
    add_to_insurance_history,
    get_insurance_calculate_history,
)
from src.insurance.exceptions import ApplicableRateNotFoundError
from src.insurance.schemas import (
    InsuranceCalculateRequest,
    InsuranceHistoryItem,
)
from src.rates.schemas import RateResponse
from src.rates.services import get_available_rates_service
from src.utils.models.models import InsuranceHistory


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

    await add_to_insurance_history(
        item=InsuranceHistory(
            cargo_type=insurance_data.cargo_type,
            declared_value=insurance_data.declared_value,
            insurance_cost=insurance_cost,
        ),
        session=session,
    )

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


async def get_insurance_calculate_history_service(
    session: AsyncSession,
    cargo_type: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
) -> List[InsuranceHistoryItem]:
    return await get_insurance_calculate_history(
        session=session,
        cargo_type=cargo_type,
        start_date=start_date,
        end_date=end_date,
    )
