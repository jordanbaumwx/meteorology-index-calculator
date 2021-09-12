import numpy as np

def saturation_vapor_pressure(temperature):
     # Temperature in Celsius
    # Code modeled after the Clausius-Clapeyron equation found here:
    # https://glossary.ametsoc.org/wiki/Clausius-clapeyron_equation
    alpha = 17.67*temperature/ (temperature + 243.5)
    
    e = 611.2 * np.exp(alpha)
    return e

def relative_humidity(temperature, dewpoint):
    # Temperature and Dewpoint in Celsius
    # Relative humidity is defined as the ratio of the vapor pressure to the saturation vapor pressure with respect to water.
    # Source: https://glossary.ametsoc.org/wiki/Relative_humidity
    if temperature is None or dewpoint is None:
        raise Exception("Cannot run with missing temperature and/or dewpoint values.")

    e = saturation_vapor_pressure(dewpoint)
    es = saturation_vapor_pressure(temperature)

    return e / es



import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)