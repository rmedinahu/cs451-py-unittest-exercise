# test_geolocwrapper.py
import unittest

from geolocwrapper import GeoLocWrapper
from geopy.exc import GeopyError


class TestGeoLocWrapper(unittest.TestCase):
    """A collection of unit tests for the BabySet class. 
    Used to demonstrate and introduce unit testing in Python.
    Related docs: https://docs.python.org/3/library/unittest.html
    """
    def test_init(self):
        """Unit test for GeoLocWrapper constructor."""
        loc = GeoLocWrapper('1701 bryant st, denver, co')
        self.assertEqual(loc.location.latitude, 39.743952)

    def test_init_fail(self):
        with self.assertRaises(GeopyError):
            loc = GeoLocWrapper()

    # Begin adding your unit tests for the GeoLocWrapper module.

if __name__ == '__main__':
    unittest.main()