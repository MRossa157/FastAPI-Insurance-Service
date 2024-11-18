# FastAPI Insurance Service

## Описание проекта

FastAPI Insurance Service — это REST API-сервис для управления тарифами и расчёта стоимости страхования грузов. Сервис поддерживает загрузку тарифов через JSON, фильтрацию данных и расчёт страховки на основе объявленной стоимости груза и актуального тарифа.

Основные возможности:
- **Загрузка тарифов**: через API в формате JSON.
- **Фильтрация тарифов**: по типу груза и дате.
- **Расчёт страховки**: по объявленной стоимости груза с учётом действующего тарифа.
- **Получение истории расчётов**.

## Установка и запуск

### 1. Клонирование репозитория

Склонируйте проект с GitHub:

```bash
git clone https://github.com/MRossa157/FastAPI-Insurance-Service.git
cd fastapi-insurance-service
```

### 2. Установка зависимостей и запуск
```bash
pip install poetry
poetry install
make app
```

**[!]** Если на этом этапе произошла ошибка, то **см. пункт 3**, а после чего пропишите `make app` еще раз.
### 3. Настройка .env файла
Переименуйте `.env.example` в `.env` и поменяйте значения переменных (не обязательно менять данные о переменных, проект поднимется и на стандартных значениях).

### 4. Настройка базы данных (нужна только при первом запуске)
1. Зайдите в контейнер базы данных:

```bash
docker exec -it postgres_db_backend bash
```

2. Выполните команду для подключения к PostgreSQL

```bash
psql --username={USERNAME} --dbname={DB_NAME}
```
- Параметры `USERNAME` и `DB_NAME` берутся из файла `.env`.

- В репозитории есть пример файла `.env.example`, который можно использовать для настройки.

3. Перезапустите контейнер приложения
```bash
make app-down
make app
```

### 5. Доступ к документации
После запуска приложение доступно по адресу:

```bash
{$BACK_HOST}:{$BACK_PORT}/docs
```
По умолчанию:
```bash
127.0.0.1:5002/docs
```

Переменные `BACK_HOST` и `BACK_PORT` настраиваются в файле `.env`.

## Технологии

Проект построен с использованием следующих технологий:
- **FastAPI**: для реализации REST API.
- **SQLAlchemy**: ORM для взаимодействия с базой данных.
- **PostgreSQL**: база данных.
- **Docker и Docker Compose**: для контейнеризации.
- **Poetry**: для управления зависимостями.
- **Makefile**: для упрощения команд развертывания.
