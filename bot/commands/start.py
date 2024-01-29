from aiogram import Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.db import create_user, get_user
from bot.keyboards import reply_back_btn
from bot.main import dp, _


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext, bot: Bot) -> None:
    """
    This handler receives messages with `/start` command
    """
    telegram_id = message.from_user.id
    user = get_user(telegram_id=telegram_id)
    if user is None:
        user = create_user(
            telegram_id=telegram_id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )

    await bot.send_message(
        chat_id=telegram_id,
        text=_('start_command_message', locale=user.get_lang()),
        reply_markup=reply_back_btn(lang=user.get_lang()),
    ),

    await state.clear()
