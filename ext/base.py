from typing import Any, Dict, Generic, Type

import orjson
from pydantic.types import UUID4
from starlite.dto import DTO
from starlite.types import Partial
from tortoise.contrib.pydantic.base import PydanticListModel, PydanticModel
from tortoise.queryset import QuerySet

from ext.types import TModel



class BaseRepository(Generic[TModel]):
    db_model: Type[TModel]
    pydantic_list_model: Type[PydanticListModel]
    pydantic_model: Type[PydanticModel]

    async def get_many(self, offset: int | None, limit: int | None) -> QuerySet[TModel] :
        if offset and limit:
            return self.db_model.all().offset(offset=offset).limit(limit=limit)
        return self.db_model.all()

    async def get_by_id(self, id: UUID4) -> TModel:
        return await self.db_model.get(id=id)

    async def create(self, data: DTO):
        raise NotImplementedError()

    async def update(self, id: UUID4, data: Partial[DTO[PydanticModel]]):
        raise NotImplementedError()

    async def delete(self, id: UUID4) -> None:
        model: TModel = await self.db_model.get(id=id)
        await model.delete()

    async def serialize_query_set(self, query_set: QuerySet[TModel]) -> Dict[str, Any]:
        models: PydanticListModel = await self.pydantic_list_model.from_queryset(query_set)
        return await self._serialize(obj=models)

    async def serialize_model(self, obj: TModel) -> Dict[str, Any]:
        model: PydanticModel = await self.pydantic_model.from_tortoise_orm(obj=obj)
        return await self._serialize(obj=model)

    async def _serialize(self, obj: PydanticListModel | PydanticModel):
        content: Dict[str, Any] = {}
        content = obj.schema()
        content["data"] = orjson.loads(obj.json())
        return content
