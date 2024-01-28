from pathlib import Path

DEBUG = True

if DEBUG:
    # demo
    BOT_TOKEN = ""
    BOT_USERNAME = "@"
    BOT_LINK = "https://t.me/"

    DATABASE_HOSTNAME = "127.0.0.1"
    DATABASE_PORT = "5432"
    DATABASE_USERNAME = "postgres"
    DATABASE_PASSWORD = ""
    DATABASE_NAME = "bot_db"
else:
    # production
    BOT_TOKEN = ""
    BOT_USERNAME = ""
    BOT_LINK = ""

    DATABASE_HOSTNAME = ""
    DATABASE_PORT = ""
    DATABASE_USERNAME = ""
    DATABASE_PASSWORD = ""
    DATABASE_NAME = ""

I18N_DOMAIN = "messages"
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'
