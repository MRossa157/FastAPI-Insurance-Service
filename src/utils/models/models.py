from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rates(Base):
    __tablename__ = 'rates'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    date = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment='Дата загрузки тарифов',
    )
    cargo_type = Column(
        String,
        nullable=False,
        comment='Тип груза',
    )
    rate = Column(
        Float,
        nullable=False,
        comment='Тариф',
    )


class InsuranceHistory(Base):
    __tablename__ = 'insurance_calculate_history'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    date = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment='Дата расчета страховки',
    )
    cargo_type = Column(
        String,
        nullable=False,
        comment='Тип груза',
    )
    declared_value = Column(
        Float,
        nullable=False,
        comment='Объявленное значение груза',
    )
    insurance_cost = Column(
        Float,
        nullable=False,
        comment='Стоимость страховки',
    )
