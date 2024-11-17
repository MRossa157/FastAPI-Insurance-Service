from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel, RootModel, field_validator

from src.rates.exceptions import InvalidKeyFormatError
from src.schemas import BaseResponse


class CargoInfo(BaseModel):
    cargo_type: str
    rate: float


class RateResponse(CargoInfo):
    effective_date: datetime


class RatesUpload(RootModel[Dict[datetime, List[CargoInfo]]]):
    @field_validator('root', mode='before')
    @classmethod
    def check_datetime_keys(
        cls,
        value: Dict[str, List[CargoInfo]],
    ) -> Dict[datetime, List[CargoInfo]]:
        converted_dict = {}
        for key, cargos in value.items():
            try:
                date_key = datetime.strptime(key, '%Y-%m-%d')
            except ValueError:
                raise InvalidKeyFormatError(key=key)

            converted_dict[date_key] = cargos

        return converted_dict


class RatesUploadResponse(BaseResponse):
    message: str = 'Rates successfully uploaded.'
