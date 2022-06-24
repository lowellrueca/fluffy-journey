import orjson
from tortoise.queryset import QuerySet
from tortoise.contrib.pydantic.base import PydanticListModel, PydanticModel
from tortoise.models import Model
from typing import Any, Dict, Type


class BaseRepository:
    db_model: Type[Model]
    ls_model: Type[PydanticListModel]

    async def get_all(self) -> QuerySet[Model]:
        return self.db_model.all()

    async def get_by_offset_limit(self, offset: int, limit: int) -> QuerySet[Model]:
        return self.db_model.all().offset(offset=offset).limit(limit=limit)

    async def serialize_query_set(self, query_set: QuerySet[Model]) -> Any:
        models: PydanticListModel = await self.ls_model.from_queryset(query_set)
        content: Dict[str, Any] = {}
        content = models.schema()
        content["data"] = orjson.loads(models.json())
        return content
