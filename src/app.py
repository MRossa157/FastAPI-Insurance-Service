from os import environ

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.rates.views import router as rates_router
from src.security import cors_settings

app = FastAPI(
    title='Insurance Service',
)

app.include_router(
    rates_router,
    prefix='/rates',
    tags=['rates'],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_settings.origins,
    allow_credentials=cors_settings.credentials,
    allow_methods=cors_settings.methods,
    allow_headers=cors_settings.headers,
)

environ['TZ'] = 'Europe/Saratov'
