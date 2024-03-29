from classic.messaging_kombu import KombuPublisher
from classic.sql_storage import TransactionContext
from kombu import Connection
from sqlalchemy import create_engine

from adapters import database, books_api, message_bus
from adapters.database import repositories
from application import services


class Settings:
    db = database.Settings()
    book_api = books_api.Settings()
    message_bus = message_bus.Settings()

class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    books_repo = repositories.BooksRepo(context=context)

class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )



class Application:
    book = services.Book(books_repo=DB.books_repo,
                         publisher=MessageBus.publisher)

    is_dev_mode = Settings.book_api.IS_DEV_MODE
    allow_origins = Settings.book_api.ALLOW_ORIGINS


class Aspects:
    services.join_points.join(DB.context)
    books_api.join_points.join(MessageBus.publisher, DB.context)


app = books_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    allow_origins=Application.allow_origins,
    book=Application.book,

)
