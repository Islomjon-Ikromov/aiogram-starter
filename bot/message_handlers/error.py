from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards import inline_back_btn
from bot.main import dp


@dp.message()
async def error_mh(message: Message, state: FSMContext, bot: Bot) -> None:
    text = message.text
    await message.answer(text, reply_markup=inline_back_btn(lang="uz"))
