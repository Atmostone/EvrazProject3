from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    BROKER_URL = "amqp://user:password@rabbitmq:5672//"

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
