from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from bot.db.database import Base


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    level = Column(String(50))
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.message
