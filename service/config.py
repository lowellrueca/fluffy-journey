from os import path
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from starlette.config import Config


env_file = path.abspath(".env")
configuration = Config(env_file=env_file)

DB_PROV = configuration(key="DB_PROV", cast=str, default="sqlite")
DB_USER = configuration(key="DB_USER", cast=str, default="user")
DB_PSWD = configuration(key="DB_PSWD", cast=Secret, default="1234")
DB_HOST = configuration(key="DB_HOST", cast=str, default="localhost")
DB_SERV = configuration(key="DB_SERV", cast=str, default="localhost")
DB_PORT = configuration(key="DB_PORT", cast=int, default=5678)
DB_NAME = configuration(key="DB_NAME", cast=str, default="db")
DEBUG = configuration(key="DEBUG", cast=bool, default=False)
HOST = configuration(key="HOST", cast=CommaSeparatedStrings, default="localhost")
PORT = configuration(key="PORT", cast=int, default=5000)


def set_db_url(
    provider: str, user: str, password: str, host: str, port: int, db_name: str
) -> str:
    return f"{provider}://{user}:{password}@{host}:{port}/{db_name}"


DB_CONFIG = {
    "connections": {
        "default": set_db_url(
            DB_PROV,
            DB_USER,
            str(DB_PSWD),
            DB_SERV,
            DB_PORT,
            DB_NAME,
        ),
    },
    "apps": {"models": {"models": ["service.models.db"]}},
}


AERICH_CONFIG = {
    "connections": {
        "default": set_db_url(
            DB_PROV,
            DB_USER,
            str(DB_PSWD),
            DB_HOST,
            DB_PORT,
            DB_NAME,
        ),
    },
    "apps": {"models": {"models": ["service.models.db", "aerich.models"]}},
}
