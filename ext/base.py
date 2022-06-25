from typing import Any, Dict, Generic, Type

import orjson
from pydantic.types import UUID4
from starlite.dto import DTO
from starlite.types import Partial
from tortoise.contrib.pydantic.base import PydanticListModel, PydanticModel
from tortoise.queryset import QuerySet

from ext.types import TModel


class BaseRepository:
    db_model: Type[Model]
    pydantic_list_model: Type[PydanticListModel]
    pydantic_model: Type[PydanticModel]

    async def get_all(self) -> QuerySet[Model]:
        return self.db_model.all()

    async def get_by_offset_limit(self, offset: int, limit: int) -> QuerySet[Model]:
        return self.db_model.all().offset(offset=offset).limit(limit=limit)

    async def get_by_id(self, id:UUID4) -> Model:
        return await self.db_model.get(id=id)

    async def serialize_query_set(self, query_set: QuerySet[Model]) -> Any:
        models: PydanticListModel = await self.pydantic_list_model.from_queryset(query_set)
        return await self._serialize(obj=models)

    async def serialize_model(self, obj: Model) -> Dict[str, Any]:
        model: PydanticModel = await self.pydantic_model.from_tortoise_orm(obj=obj)
        return await self._serialize(obj=model)

    async def _serialize(self, obj: PydanticListModel | PydanticModel):
        content: Dict[str, Any] = {}
        content = obj.schema()
        content["data"] = orjson.loads(obj.json())
        return content
