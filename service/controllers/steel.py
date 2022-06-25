from typing import Any, Dict

from pydantic.types import UUID4
from starlette.exceptions import HTTPException
from starlite import Controller, Parameter, Provide, delete, get, patch, post
from starlite.types import Partial
from tortoise.exceptions import DoesNotExist
from tortoise.models import Model
from tortoise.queryset import QuerySet

from service.repository import SteelRepository
from service.models import Steel, SteelDTO


class SteelController(Controller):
    path = "/steel"
    dependencies = {"repository": Provide(SteelRepository)}

    @get(path="/")
    async def get_products(
            self, 
            repository: SteelRepository,
            page_number: int = Parameter(query="pageNumber", default=1), 
            page_size: int = Parameter(query="pageSize", default=24, gt=0, le=50)
        ) -> Dict[str, Any] | None:

        query_set: QuerySet[Steel] = await repository.get_many(offset=page_number, limit=page_size)
        return await repository.serialize_query_set(query_set=query_set) 

    @get(path="/{product_id:uuid}")
    async def get_product_by_id(self, repository: SteelRepository, product_id: UUID4) -> Dict[str, Any]:
        try:
            model: Model | Steel = await repository.get_by_id(id=product_id)
            return await repository.serialize_model(obj=model)

        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Product not found")

    @post(path="/")
    async def create_product(self, repository: SteelRepository, data: SteelDTO) -> Dict[str, Any]:
        model: Steel = await repository.create(data=data)
        return await repository.serialize_model(obj=model)
 
    @patch(path="/{product_id:uuid}")
    async def update_product(self, repository: SteelRepository, product_id: UUID4, data: Partial[SteelDTO]) -> Dict[str, Any]:
        try:
            model: Steel = await repository.update(id=product_id, data=data)
            return await repository.serialize_model(obj=model)

        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Product not found")

    @delete(path="/{product_id:uuid}")
    async def delete_product(self, repository: SteelRepository, product_id: UUID4) -> None:
        try:
            await repository.delete(id=product_id)

        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Product not found")
