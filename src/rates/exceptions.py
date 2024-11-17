from fastapi import HTTPException

from src.exceptions import AppError


class InvalidKeyFormatError(AppError, HTTPException):
    """Ошибка неверного формата ключа."""
    def __init__(self, key: str):
        detail = f"Key '{key}' is not in valid format 'YYYY-MM-DD'."
        AppError.__init__(self, detail=detail)
        HTTPException.__init__(self, status_code=422, detail=detail)


class RateNotFoundError(AppError, HTTPException):
    """Ошибка, возникающая, если тариф не найден."""
    def __init__(self, rate_id: int):
        detail = f'Rate with id {rate_id} not found'
        AppError.__init__(self, detail=detail)
        HTTPException.__init__(self, status_code=404, detail=detail)
