from ext import BaseRepository
from service.models import Steel, SteelModel, SteelModelQuerySet
from typing import Type


class SteelRepository(BaseRepository):
    db_model: Type[Steel] = Steel
    pydantic_list_model: Type[SteelModelQuerySet] = SteelModelQuerySet
    pydantic_model: Type[SteelModel] = SteelModel
