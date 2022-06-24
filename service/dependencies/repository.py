from ext import BaseRepository
from service.models import Steel, SteelModelQuerySet
from typing import Type


class SteelRepository(BaseRepository):
    db_model: Type[Steel] = Steel
    ls_model: Type[SteelModelQuerySet] = SteelModelQuerySet
