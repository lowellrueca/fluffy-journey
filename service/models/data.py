import random


async def seed_data():
    from service.models import Steel
    
    models = await Steel.all()
    random_names = ["i-beam", "shs", "rhs", "flat_bar", "chs", "pipe", "c-channel"]
    mock_products = [Steel(name=random.choice(random_names)) for i in range(300) if len(models) == 0]
    await Steel.bulk_create(mock_products)

