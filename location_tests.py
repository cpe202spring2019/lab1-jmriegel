import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc1
        self.assertEqual(loc1, loc3)
        self.assertEqual(loc1, loc4)




if __name__ == "__main__":
        unittest.main()
