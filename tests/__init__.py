import unittest
from functools import wraps

from peewee import SqliteDatabase

from models import APP_MODELS, db

test_db = SqliteDatabase('test_database.db')


class AppTestCase(unittest.TestCase):
    """
    Base class for tskwish test cases.
    """
    
    def setUp(self):
        test_db.bind(APP_MODELS)
        test_db.create_tables(APP_MODELS)

    def tearDown(self):
        test_db.drop_tables(APP_MODELS)
        db.bind(APP_MODELS)