import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.config import BOT_TOKEN, LOCALES_DIR, I18N_DOMAIN
from bot.db import database, models

scheduler = AsyncIOScheduler()

dp = Dispatcher()
bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)

router = Router()
i18n = I18n(path=LOCALES_DIR, default_locale="uz", domain=I18N_DOMAIN)
md = SimpleI18nMiddleware(i18n)
_ = i18n.gettext


def set_database():
    models.Base.metadata.create_all(bind=database.engine)
    logging.basicConfig(level=logging.INFO)


async def set_commands(lang: str):
    commands = [
        BotCommand(command="/start", description=f"♻️ {_('start_text', locale=lang)}"),
    ]
    await bot.set_my_commands(commands)


def register_commands():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(set_commands(lang='uz'))


# def set_schedules():
#     scheduler.start()

class DatabaseHandler(logging.Handler):

    def __init__(self):
        super().__init__()

    def emit(self, record):
        from bot.db import GetDB

        level = record.levelname
        message = self.format(record)

        try:
            with GetDB() as db:
                db_log = models.Log(
                    level=level,
                    message=message,
                )
                db.add(db_log)
                db.commit()

        except Exception as e:
            print(f"Error writing log to database: {e}")


async def main() -> None:
    # set logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    db_handler = DatabaseHandler()
    db_handler.setLevel(logging.DEBUG)
    logging.getLogger().addHandler(db_handler)

    # set i18n
    router.message.middleware(middleware=md)

    # set database
    set_database()

    # set commands
    await set_commands(lang='uz')

    # set schedules
    # set_schedules()

    # run bot as polling
    await dp.start_polling(bot)
