import unittest

from models import Vector
from tests import AppTestCase


class TestVector(AppTestCase):

    def test_create_vector(self):
        """
        Vectors should retain their data after being created.
        """
        values = [1.2123, 34545.33, 45656.33, 999.9999, 8238823.00001]
        vector = Vector.create(values=values)
        self.assertEqual(values, vector.as_list())


if __name__ == '__main__':
    unittest.main()