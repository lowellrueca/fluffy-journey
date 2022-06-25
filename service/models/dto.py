""" Contains data pydantic models """

from service.models import Steel
from starlite import DTOFactory
from tortoise.contrib.pydantic.base import PydanticListModel, PydanticModel
from tortoise.contrib.pydantic.creator import pydantic_model_creator, pydantic_queryset_creator
from typing import Type


dto_factory: DTOFactory = DTOFactory()

SteelModel: Type[PydanticModel] = pydantic_model_creator(Steel)
SteelModelQuerySet: Type[PydanticListModel] = pydantic_queryset_creator(Steel)
SteelDTO = dto_factory(
    name="SteelDTO", 
    source=SteelModel, 
    field_mapping={"id": "id", "name":"name"}
)
