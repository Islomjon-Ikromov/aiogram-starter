from aiogram.filters import Filter
from aiogram.types import Message

from bot.db import get_user
from bot.main import _


class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        user = get_user(telegram_id=message.from_user.id)
        return _(f"{message.text}", locale=user.get_lang()) == _(f"{self.my_text}", locale=user.get_lang())
