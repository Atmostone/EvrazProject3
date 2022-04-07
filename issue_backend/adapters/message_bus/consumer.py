from kombu import Connection

from classic.messaging_kombu import KombuConsumer

from application import services
from .scheme import broker_scheme


def create_consumer(
    connection: Connection, issues: services.Issue
) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection, scheme=broker_scheme)

    consumer.register_function(
        issues.create_issue,
        'test',
    )

    return consumer
