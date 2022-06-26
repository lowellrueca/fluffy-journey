from tortoise.models import Model
from typing import  TypeVar


TModel = TypeVar("TModel", bound=Model)
