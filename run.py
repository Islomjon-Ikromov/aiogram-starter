import asyncio

from bot.main import main

if __name__ == "__main__":
    asyncio.run(main())

"""
pybabel extract --input-dirs=. -o locales/messages.pot
pybabel init -i locales/messages.pot -d locales -D messages -l uz
pybabel compile -d locales -D messages

pybabel extract --input-dirs=. -o locales/messages.pot
pybabel update -d locales -D messages -i locales/messages.pot
pybabel compile -d locales -D messages

"""
