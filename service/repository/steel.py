from typing import Type

from pydantic.types import UUID4
from starlite.types import Partial
from tortoise.queryset import QuerySet

from ext.base import BaseRepository
from service.models import Steel, SteelDTO, SteelModel, SteelModelQuerySet


class SteelRepository(BaseRepository):
    db_model: Type[Steel] = Steel
    pydantic_list_model: Type[SteelModelQuerySet] = SteelModelQuerySet
    pydantic_model: Type[SteelModel] = SteelModel

    async def get_many(self, offset: int | None, limit: int | None) -> QuerySet[Steel]:
        return await super().get_many(offset=offset, limit=limit)

    async def get_by_id(self, id: UUID4) ->  Steel:
        return await super().get_by_id(id=id)

    async def create(self, data: SteelDTO) -> Steel:
        name = getattr(data, "name")
        model: Steel = await self.db_model.create(name=name)
        return model

    async def update(self, id: UUID4, data: Partial[SteelDTO]) -> Steel: 
        model: Steel = await self.db_model.get(id=id)
        model.name = getattr(data, "name")
        await model.save()
        return model

    async def delete(self, id: UUID4) -> None:
        return await super().delete(id=id)
