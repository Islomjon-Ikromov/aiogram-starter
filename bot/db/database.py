from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# SQLALCHEMY_DATABASE_URL = f'postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}' \
#                           f'/{DATABASE_NAME}'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SQLALCHEMY_DATABASE_URL = f"sqlite:///database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo_pool=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class GetDB:
    def __enter__(self):
        self.db: Session = SessionLocal()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()
