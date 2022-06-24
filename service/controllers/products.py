from service.dependencies import SteelRepository
from starlite import Controller, Parameter, Provide, get
from tortoise.queryset import QuerySet
from tortoise.models import Model
from typing import Any, Dict


class ProductController(Controller):
    path = "/products"
    dependencies = {"repository": Provide(SteelRepository)}

    @get(path="/")
    async def get_products(self, repository: SteelRepository) -> Dict[str, Any]:
        query_set: QuerySet[Model] = await repository.get_all()
        return await repository.serialize_query_set(query_set=query_set)

    @get(path="/query")
    async def get_paginated_products(
            self, 
            repository: SteelRepository,
            page_number: int = Parameter(query="pageNumber"), 
            page_size: int = Parameter(query="pageSize", gt=0, le=50)
        ) -> Dict[str, Any]:

        query_set: QuerySet[Model] = await repository.get_by_offset_limit(offset=page_number, limit=page_size)
        return await repository.serialize_query_set(query_set=query_set)

    @get(path="/{product_id:int}")
    async def get_product_by_id(self, product_id: int) -> dict:
        return {"data": [{"product_id": product_id, "name": "Elsa"}]}
