""" Contains data pydantic models """

from service.models import Steel
from tortoise.contrib.pydantic.base import PydanticListModel, PydanticModel
from tortoise.contrib.pydantic.creator import pydantic_model_creator, pydantic_queryset_creator
from typing import Type


SteelModel: Type[PydanticModel] = pydantic_model_creator(Steel)
SteelModelQuerySet: Type[PydanticListModel] = pydantic_queryset_creator(Steel)
