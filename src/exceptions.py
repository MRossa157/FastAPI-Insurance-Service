from dataclasses import dataclass


@dataclass
class AppError(Exception):
    """Базовая ошибка приложения."""
    detail: str

    def __str__(self):
        return self.detail
