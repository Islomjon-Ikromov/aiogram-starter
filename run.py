import asyncio

from bot.main import main_polling, main_webhook

if __name__ == "__main__":
    asyncio.run(main_polling())
    # main_webhook()

"""
pybabel extract --input-dirs=. -o locales/messages.pot
pybabel init -i locales/messages.pot -d locales -D messages -l uz
pybabel compile -d locales -D messages

pybabel extract --input-dirs=. -o locales/messages.pot
pybabel update -d locales -D messages -i locales/messages.pot
pybabel compile -d locales -D messages

alembic revision --autogenerate -m "initial"
alembic upgrade head
"""
