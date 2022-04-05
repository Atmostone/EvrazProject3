from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from adapters import database, books_api

from adapters.database import repositories
from application import services


class Settings:
    db = database.Settings()
    book_api = books_api.Settings()

class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    books_repo = repositories.BooksRepo(context=context)

class Application:
    book = services.Book(books_repo=DB.books_repo)

    is_dev_mode = Settings.book_api.IS_DEV_MODE
    allow_origins = Settings.book_api.ALLOW_ORIGINS


class Aspects:
    services.join_points.join(DB.context)
    books_api.join_points.join(DB.context)


app = books_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    allow_origins=Application.allow_origins,
    book=Application.book,
)
