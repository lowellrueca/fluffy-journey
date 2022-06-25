from pydantic.types import UUID4
from starlite import Controller, Parameter, Provide, get, post
from service.dependencies import SteelRepository
from service.models.dto import SteelDTO
from tortoise.queryset import QuerySet
from tortoise.models import Model
from typing import Any, Dict


class ProductController(Controller):
    path = "/products"
    dependencies = {"repository": Provide(SteelRepository)}

    @get(path="/")
    async def get_products(
            self, 
            repository: SteelRepository,
            page_number: int = Parameter(query="pageNumber", default=1), 
            page_size: int = Parameter(query="pageSize", default=12, gt=0, le=50)
        ) -> Dict[str, Any]:

        query_set: QuerySet[Model] = await repository.get_by_offset_limit(offset=page_number, limit=page_size)
        return await repository.serialize_query_set(query_set=query_set)

    @get(path="/{product_id:uuid}")
    async def get_product_by_id(self, repository: SteelRepository, product_id: UUID4) -> Dict[str, Any]:
        model: Model = await repository.get_by_id(id=product_id)
        return await repository.serialize_model(obj=model)

    @post(path="/")
    async def create_product(self, repository: SteelRepository, data: SteelDTO) -> Dict[str, Any]:
        name = data.name or None
        db_model = await repository.db_model.create(name=name)
        return await repository.serialize_model(obj=db_model)
