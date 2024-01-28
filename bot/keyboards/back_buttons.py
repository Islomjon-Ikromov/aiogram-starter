from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from bot.main import _


def reply_back_btn(lang: str):
    keyboard = [
        [KeyboardButton(text="⬅️ " + _('back', locale=lang))]
    ]
    markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard, one_time_keyboard=True)

    return markup


def inline_back_btn(lang: str):
    keyboard = [
        [InlineKeyboardButton(text="⬅️ " + _('back', locale=lang), callback_data="back")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    return markup
