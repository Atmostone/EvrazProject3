import os
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    user = os.environ['RABBIT_USER']
    password = os.environ['RABBIT_PASSWORD']
    host = os.environ['RABBIT_HOST']
    port = os.environ['RABBIT_PORT']

    BROKER_URL = f"amqp://{user}:{password}@{host}:{port}//"

    LOGGING_LEVEL: str = 'INFO'

    @property
    def LOGGING_CONFIG(self):
        return {
            'loggers': {
                'kombu': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False
                }
            }
        }
