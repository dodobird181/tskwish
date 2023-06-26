from peewee import *

from models import BaseModel


class Float(BaseModel):
    """
    A table of unique floating point numbers.
    """
    value = FloatField(unique=True, primary_key=True, null=False)

    @classmethod
    def create(cls, value):
        try:
            return super().get(Float.value == value)
        except Float.DoesNotExist:
            return super().create(value=value)
