""" Contains database models """

from tortoise.models import Model
from tortoise.fields import UUIDField, CharField


class AbstractModel(Model):
    id = UUIDField(pk=True)

    class Meta:
        abstract = True


class Steel(AbstractModel):
    """ Steel Product """

    name = CharField(max_length=128, nullable=False)

    class Meta: 
        table = "steel"


__models__ = [Steel]
