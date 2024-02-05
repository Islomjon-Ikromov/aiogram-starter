from pathlib import Path

DEBUG = True

if DEBUG:
    # demo
    BOT_TOKEN = "6987000669:AAElTWayIN3kPvlizpA7mIbnP7vd4HaOkno"
    BOT_USERNAME = "@username"
    BOT_LINK = "https://t.me/username"

    DATABASE_HOSTNAME = "127.0.0.1"
    DATABASE_PORT = "5432"
    DATABASE_USERNAME = "postgres"
    DATABASE_PASSWORD = ""
    DATABASE_NAME = "bot_db"

    WEB_SERVER_HOST = "127.0.0.1"
    WEB_SERVER_PORT = 8080
    WEBHOOK_PATH = "/webhook"
    WEBHOOK_SECRET = ""
    BASE_WEBHOOK_URL = "https://96c3-92-63-205-178.ngrok-free.app"  # here put web-site url or you can use ngrok
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
