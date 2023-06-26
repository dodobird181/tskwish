from peewee import Model, SqliteDatabase

db = SqliteDatabase('app_database.db')

class BaseModel(Model):
    """
    Base model for all other database tables.
    """
    class Meta:
        database = db

from models.api_key import ApiKey
from models.float import Float
from models.vector import Vector, VectorData

print('poop!')

from models.embedding import Embedding

APP_MODELS = [
    ApiKey, 
    Float, 
    Vector,
    VectorData,
    Embedding,
]
db.connect()
db.create_tables(APP_MODELS)