from fastapi import HTTPException

from src.exceptions import AppError


class InvalidKeyFormatError(AppError, HTTPException):
    """Ошибка неверного формата ключа."""
    def __init__(self, key: str):
        detail = f"Key '{key}' is not in valid format 'YYYY-MM-DD'."
        AppError.__init__(self, detail=detail)
        HTTPException.__init__(self, status_code=422, detail=detail)
