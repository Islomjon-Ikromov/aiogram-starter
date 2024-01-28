## FastAPI Starter Project

```
├── bot
│   ├── commands
│   │   ├── start.py
│   │   └── utils.py
│   ├── db
│   │   ├── database.py
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

# Setting up the project without Docker

1. Clone the repository from GitHub.
    ```
    git clone https://github.com/Islomjon-Ikromov/aiogram-starter.git
    ```

2. Enter the cloned project folder.
    ```
    cd aiogram-starter
    ```

3. Create a virtual environment using Python's `venv` module:

    ```
    python -m venv .venv
    ```
    or
    ```
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    - For Windows:

        ```
        .\.venv\Scripts\activate.ps1
        ```

    - For Linux or macOS:

        ```
        source .venv/bin/activate
        ```

5. Install the required dependencies using `pip`:

    ```
    pip install -r requirements.txt
    ```

5. Create a database using pgadmin. ex: `fastapi_starter`

6. Update `config.py` file with your own values.
    ```
    BOT_TOKEN = ""
    BOT_USERNAME = ""
    BOT_LINK = ""

    DATABASE_HOSTNAME = ""
    DATABASE_PORT = ""
    DATABASE_USERNAME = ""
    DATABASE_PASSWORD = ""
    DATABASE_NAME = ""
    ```




7. Set up the database using alembic by running the following command:
    - makemigrations
        ```
        alembic revision --autogenerate -m "initial"
        ```
    - migrate
        ```
        alembic upgrade head
        ```

8. Start the server:

    ```
    python3 run.py | python run.py
    ```