from datetime import datetime
from typing import List, Optional

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.insurance.schemas import InsuranceHistoryItem
from src.utils.models.models import InsuranceHistory


async def add_to_insurance_history(
    session: AsyncSession,
    item: InsuranceHistory,
) -> None:
    session.add(item)
    await session.commit()


async def get_insurance_calculate_history(
    session: AsyncSession,
    cargo_type: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
) -> List[InsuranceHistoryItem]:
    query = select(InsuranceHistory).order_by(desc(InsuranceHistory.date))
    filters = []

    if cargo_type is not None:
        filters.append(InsuranceHistory.cargo_type == cargo_type)
    if start_date is not None:
        filters.append(InsuranceHistory.date >= start_date)
    if end_date is not None:
        filters.append(InsuranceHistory.date <= end_date)

    if filters:
        query = query.where(*filters)

    result = await session.execute(query)
    return [
        InsuranceHistoryItem(
            cargo_type=item.cargo_type,
            declared_value=item.declared_value,
            insurance_cost=item.insurance_cost,
            date=item.date,
        )
        for item in result.scalars().all()
    ]
