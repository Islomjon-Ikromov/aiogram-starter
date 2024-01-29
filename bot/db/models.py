from datetime import datetime

import pytz
from sqlalchemy import Column, Integer, String, DateTime, BigInteger

from bot.db.database import Base


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    level = Column(String(50))
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.message


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)  # autoincrement=True
    telegram_id = Column(BigInteger, index=True, unique=True, nullable=False)
    full_name = Column(String, index=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=True)
    username = Column(String, index=True, unique=True, nullable=True)
    state = Column(Integer, default=1)  # 1-show, 2-hide

    language = Column(String, nullable=False, default="-")
    created_at = Column(DateTime, default=datetime.now(pytz.timezone('Asia/Tashkent')), nullable=False)

    def __str__(self):
        return self.full_name

    def get_lang(self):
        if self.language == "-":
            return "uz"
        return self.language
