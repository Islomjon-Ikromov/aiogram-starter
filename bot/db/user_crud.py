from typing import Optional

from sqlalchemy import or_

from bot.db import models
from bot.db.database import GetDB


def create_user(
        telegram_id: int,
        full_name: str,
        username: Optional[str] = None,
) -> models.User:
    with GetDB() as db:
        db_user = models.User(
            telegram_id=telegram_id,
            username=username,
            full_name=full_name,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user


def get_user(
        user_id: int = None,
        telegram_id: int = None,
        phone_number: str = None,
) -> models.User:
    with GetDB() as db:
        user = db.query(models.User).filter(or_(*[
            models.User.id == user_id,
            models.User.telegram_id == telegram_id,
            models.User.phone_number == phone_number,
        ])).first()

    return user


def get_users():
    with GetDB() as db:
        users = db.query(models.User).filter(
            models.User.state == 1,
        ).all()
    return users


def update_user(
        user_id: Optional[int] = None,
        telegram_id: Optional[int] = None,
        full_name: Optional[str] = None,
        username: Optional[str] = None,
        phone_number: Optional[str] = None,
        language: Optional[str] = None,
        state: Optional[int] = None,
):
    with GetDB() as db:
        user = db.query(models.User).filter(or_(*[
            models.User.id == user_id,
            models.User.telegram_id == telegram_id,
        ])).first()

        if user is None:
            return None

        if full_name:
            user.full_name = full_name
        if phone_number:
            user.phone_number = phone_number
        if username:
            user.username = username
        if language:
            user.language = language
        if state:
            user.state = state

        db.commit()
        db.refresh(user)
    return user
