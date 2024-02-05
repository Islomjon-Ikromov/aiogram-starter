import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.config import BOT_TOKEN, LOCALES_DIR, I18N_DOMAIN, WEBHOOK_SECRET, BASE_WEBHOOK_URL, WEBHOOK_PATH, \
    WEB_SERVER_HOST, WEB_SERVER_PORT
from bot.db import database, models

scheduler = AsyncIOScheduler()

try:
    dp = Dispatcher()
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    router = Router()

    app = web.Application()
except Exception as e:
    print(e)

i18n = I18n(path=LOCALES_DIR, default_locale="uz", domain=I18N_DOMAIN)
md = SimpleI18nMiddleware(i18n)
_ = i18n.gettext


def set_database():
    models.Base.metadata.create_all(bind=database.engine)
    logging.basicConfig(level=logging.INFO)


async def set_commands(lang: str = "uz"):
    commands = [
        BotCommand(command="/start", description=f"♻️ {_('start_text', locale=lang)}"),
    ]
    await bot.set_my_commands(commands)


def set_schedules():
    # scheduler.add_job(function_name, 'interval', minutes=10)
    scheduler.start()


async def on_startup() -> None:
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)


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


async def main_polling() -> None:
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
    set_schedules()

    # run bot as polling
    await dp.start_polling(bot)


def main_webhook() -> None:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    db_handler = DatabaseHandler()
    db_handler.setLevel(logging.DEBUG)
    logging.getLogger().addHandler(db_handler)

    # set database
    set_database()

    # set commands
    dp.startup.register(set_commands)

    # set schedules
    set_schedules()

    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)

    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )

    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)
