from aiogram.filters import Filter
from aiogram.types import Message

from bot.main import _


class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return _(f"{message.text}", locale="uz") == _(f"{self.my_text}", locale="uz")
