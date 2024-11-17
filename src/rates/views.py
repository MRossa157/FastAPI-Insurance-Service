from fastapi import APIRouter

from src.rates.schemas import RatesUpload, RatesUploadResponse

router = APIRouter()

@router.post(
    path='/upload',
    summary='Загрузить информацию о тарифах',
)
def upload_rates(rates_info: RatesUpload) -> RatesUploadResponse:
    return RatesUploadResponse
