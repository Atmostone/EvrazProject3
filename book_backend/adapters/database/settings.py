from pydantic import BaseSettings


class Settings(BaseSettings):
    user = 'postgres'
    password = 'postgres'
    host = 'db'
    port = '5432'
    database = 'bootcamp'

    DB_URL: str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

    LOGGING_LEVEL: str = 'INFO'
    SA_LOGS: bool = False

    @property
    def LOGGING_CONFIG(self):
        config = {
            'loggers': {
                'alembic': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False
                }
            }
        }

        if self.SA_LOGS:
            config['loggers']['sqlalchemy'] = {
                'handlers': ['default'],
                'level': self.LOGGING_LEVEL,
                'propagate': False
            }

        return config
