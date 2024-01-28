from aiogram import Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards import reply_back_btn
from bot.main import dp, _


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext, bot: Bot) -> None:
    """
    This handler receives messages with `/start` command
    """
    telegram_id = message.from_user.id

    await bot.send_message(
        chat_id=telegram_id,
        text=_('start_command_message', locale="uz"),
        reply_markup=reply_back_btn(lang="uz"),
    ),

    await state.clear()
