from __future__ import annotations

from typing import List

from peewee import FloatField, IntegerField

from models import BaseModel, Float


class Vector(BaseModel):
    """
    Empty model with id (provided automatically by peewee) that
    represents a vector of floating-point numbers. Data is stored
    in the `VectorData` table.
    """
    
    @classmethod
    def create(cls, values: List[float]) -> Vector:
        """
        Create a new `Vector` with the given floating-point values.
        """
        vector = super().create()  # No data passed
        for value in values:
            float = Float.create(value=value)
            VectorData.create(vid=vector.id, fid=float.value)
        return vector
    
    def as_list(self) -> List[float]:
        """
        Return an ordered list of floating-point numbers in this vector.
        """
        vid = self.id
        data = VectorData.filter(VectorData.vid == vid)
        return [datapoint.fid for datapoint in data]


class VectorData(BaseModel):
    """
    One-to-one links between rows on the `Vector` and `Float` tables.
    """
    vid = IntegerField(null=False)
    fid = FloatField(null=False)
