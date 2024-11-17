from datetime import datetime
from typing import List, Optional

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from src.utils.models.models import Rates


async def add_rates(rates: List[Rates], session: AsyncSession) -> None:
    session.add_all(rates)
    await session.commit()


async def get_rates(
    session: AsyncSession,
    cargo_type: Optional[str],
    effective_date: Optional[datetime],
) -> List[Rates]:
    if cargo_type or effective_date:
        base_query = select(Rates).order_by(desc(Rates.date))
        if cargo_type:
            base_query = base_query.where(Rates.cargo_type == cargo_type)
        if effective_date:
            base_query = base_query.where(Rates.date == effective_date)
    else:
        subquery = (
            select(Rates)
            .distinct(Rates.cargo_type)
            .order_by(Rates.cargo_type, desc(Rates.date))
            .subquery()
        )
        aliased_rates = aliased(Rates, subquery)
        base_query = select(aliased_rates).order_by(desc(aliased_rates.date))

    result = await session.execute(base_query)
    return result.scalars().all()
