import orjson
from tortoise.queryset import QuerySet
from tortoise.contrib.pydantic.base import PydanticListModel, PydanticModel
from tortoise.models import Model
from typing import Any, Dict, Type


class BaseRepository:
    db_model: Type[Model]
    pydantic_list_model: Type[PydanticListModel]
    pydantic_model: Type[PydanticModel]

    async def get_all(self) -> QuerySet[Model]:
        return self.db_model.all()

    async def get_by_offset_limit(self, offset: int, limit: int) -> QuerySet[Model]:
        return self.db_model.all().offset(offset=offset).limit(limit=limit)

    async def serialize_query_set(self, query_set: QuerySet[Model]) -> Any:
        models: PydanticListModel = await self.pydantic_list_model.from_queryset(query_set)
    async def serialize_model(self, obj: Model) -> Dict[str, Any]:
        model: PydanticModel = await self.pydantic_model.from_tortoise_orm(obj=obj)
        content: Dict[str, Any] = {}
        content = models.schema()
        content["data"] = orjson.loads(models.json())
        return content
