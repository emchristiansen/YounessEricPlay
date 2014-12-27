# This file tests lib.py.

import unittest

class TestGoogleAPI(unittest.TestCase):
    def setUp(self):
        pass

    def test_api_call_returns_sane_result(self):
        self.assertEqual(False, True)

if __name__ == '__main__':
    unittest.main()
