# This file tests lib.py.

import unittest

from lib import *

class TestGoogleAPI(unittest.TestCase):
    def setUp(self):
        pass

    def test_time_in_hours_between_locations(self):
        # TODO(youness)
        start = "Carlsbad, California"
        stop = "San Francisco, California"

        hours = time_in_hours_between_locations(start, stop)

        print(hours)

        self.assertGreater(hours, 4.0)
        self.assertLess(hours, 16.0)

if __name__ == '__main__':
    unittest.main()
