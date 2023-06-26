import unittest

from models import Float
from tests import AppTestCase


class TestFloat(AppTestCase):

    def test_create_float(self):
        """
        Floats should be unique in the database based on their value.
        If multiple floats would be created using the same value, a single
        float with that value should be created instead.
        """
        f1 = Float.create(value=12.345678910)
        f2 = Float.create(value=12.345678910)
        all_floats = [float for float in Float]
        self.assertEqual(len(all_floats), 1)
        self.assertEqual(all_floats[0].value, f1.value)
        self.assertEqual(all_floats[0].value, f2.value)
        

if __name__ == '__main__':
    unittest.main()