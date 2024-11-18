from fastapi import HTTPException

from src.exceptions import AppError


class ApplicableRateNotFoundError(AppError, HTTPException):
    """Ошибка, возникающая, если подходящий тариф не найден."""

    def __init__(self, cargo_type: str, date: str):
        detail = (
            f"No applicable rate found for the given cargo type '{cargo_type}' "
            f"and date '{date}'."
        )
        AppError.__init__(self, detail=detail)
        HTTPException.__init__(self, status_code=404, detail=detail)
