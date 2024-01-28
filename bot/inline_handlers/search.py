from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineQuery

from bot.main import dp


@dp.inline_query(lambda inline_query: len(inline_query.query) > 0)
async def search_ih(inline_query: InlineQuery, state: FSMContext, bot: Bot):
    query = inline_query.query
    print(query)
