from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.filters import MyFilter
from bot.main import dp


@dp.message(MyFilter("back"))
async def back_mh(message: Message, state: FSMContext, bot: Bot) -> None:
    telegram_id = message.from_user.id
    print(state)
    await bot.send_message(
        chat_id=telegram_id,
        text="it is back",
    )
