from classic.messaging_kombu import KombuPublisher
from kombu import Connection
from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from adapters import database, issues_api, message_bus

from adapters.database import repositories
from application import services


class Settings:
    db = database.Settings()
    issues_api = issues_api.Settings()
    message_bus = message_bus.Settings()

class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    issues_repo = repositories.IssueRepo(context=context)

class Application:
    issue = services.Issue(issues_repo=DB.issues_repo,)

    is_dev_mode = Settings.issues_api.IS_DEV_MODE
    allow_origins = Settings.issues_api.ALLOW_ORIGINS



class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )


class Aspects:
    services.join_points.join(DB.context)
    issues_api.join_points.join(DB.context)


app = issues_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    allow_origins=Application.allow_origins,
    issue=Application.issue,
)
