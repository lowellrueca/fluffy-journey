from tortoise import Tortoise


async def on_startup():
    from service.config import DB_CONFIG
    from service.models import seed_data

    await Tortoise.init(config=DB_CONFIG)
    await Tortoise.generate_schemas()
    await seed_data()


async def on_shutdown():
    await Tortoise.close_connections()
