from service.models import Steel
from tortoise.models import Model
from typing import  TypeVar


TModel = TypeVar("TModel", bound=Model | Steel)
