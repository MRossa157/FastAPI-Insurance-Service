from fastapi import APIRouter

router = APIRouter()


@router.post(
    path='/calculate',
    summary='Рассчитать стоимость страхования для груза',
)
async def calculate_insurance(): ...

@router.get(
    path='/history',
    summary='Получить историю расчетов',
)
async def history_insurance(): ...