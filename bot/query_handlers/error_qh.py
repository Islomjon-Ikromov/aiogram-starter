from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.main import dp


@dp.callback_query()
async def error_qh(call: CallbackQuery, state: FSMContext, bot: Bot) -> None:
    data = call.data
    await call.answer(data)
