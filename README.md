## Aiogram3 Starter Project

```
├── bot
│   ├── commands
│   │   ├── start.py
│   ├── db
│   │   ├── database.py
│   │   ├── users_crud.py
│   │   └── models.py
│   ├── inline_handlers
│   │   └── serach.py
│   ├── keyboards
│   │   └── back_buttons.py
│   ├── locales
│   │   └── uz
│   ├── message_handlers
│   │   ├── back_mh.py
│   │   └── error_mh.py
│   ├── query_handlers
│   │   └── error_qh.py
│   ├── schedules
│   ├── states
│   │   └── user.py
│   ├── utils
├── Dockerfile
├── run.py
├── config.py
├── filters.py
├── README.md
├── alembic.ini
└── requirements.txt
```

# Setting up the project

1. Clone the repository from GitHub.
    ```
    git clone https://github.com/Islomjon-Ikromov/aiogram-starter.git
    ```

2. Create a virtual environment using Python's `venv` module:

    ```
    python -m venv ./venv
    ```
    or
    ```
    python3 -m venv ./venv
    ```
   
3. Enter the cloned project folder.
    ```
    cd aiogram-starter
    ```


4. Activate the virtual environment:

    - For Windows:

        ```
        ..\venv\Scripts\activate
        ```

    - For Linux or macOS:

        ```
        source ../venv/bin/activate
        ```

5. Install the required dependencies using `pip`:

    ```
    pip install -r requirements.txt
    ```

6. Update `config.py` file with your own values.
    ```
    BOT_TOKEN = ""
    BOT_USERNAME = ""
    BOT_LINK = ""
    ```
   Not required this config
    ```
    DATABASE_HOSTNAME = "" 
    DATABASE_PORT = ""
    DATABASE_USERNAME = ""
    DATABASE_PASSWORD = ""
    DATABASE_NAME = ""
    ```
7. Set up the database using alembic by running the following command:

    - makemigrations:

        ```
        alembic revision --autogenerate -m "initial"
        ```

    - migrate:

        ```
        alembic upgrade head
        ```

8. Start the bot:

   ```
    python3 run.py
   ```
   or
   ```
   python3 run.py
   ```