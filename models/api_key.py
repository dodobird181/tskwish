from peewee import *

from models import BaseModel


class ApiKey(BaseModel):
    """
    Table for storing API keys.
    """
    value = CharField(unique=True)
