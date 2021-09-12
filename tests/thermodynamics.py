import sys
  
# Append to get package modules
sys.path.append("..")

from thermodynamics.moisture import relative_humidity

import unittest

class TestMoistureThermodynamics(unittest.TestCase):
    def test_relative_humidity_profile_full(self):
        self.assertEqual(int(relative_humidity(100, 100)), 1)

    def test_relative_humidity_profile_none(self):
        self.assertEqual(int(relative_humidity(-273.15, 100)), 0)

    def test_relative_humidity_profile_TdOverT(self):
        self.assertEqual(int(relative_humidity(-273.15, 100)), 0)

if __name__ == '__main__':
    unittest.main()