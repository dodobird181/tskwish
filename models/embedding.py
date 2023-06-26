from __future__ import annotations

import uuid
from datetime import datetime

from peewee import DateTimeField, ForeignKeyField, TextField, UUIDField

from gpt import get_embedding
from models import BaseModel, Vector


class Embedding(BaseModel):
    """
    Vector text embedding.
    """
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    vector = ForeignKeyField(Vector, null=False)
    text = TextField(null=False)

    @classmethod
    def create(cls, text: str) -> Embedding:
        """
        Create a new vector embedding for the given text using GPT's 
        Embeddings endpoint.
        """
        values = get_embedding(text)
        vector = Vector.create(values=values)
        return super().create(vector=vector, text=text)

