"""
pypredictor 0.1.0

© Hamd Waseem under the Apache Licence 2.0

numpredict_tests.py - Tests numpredict.py
"""

import pypredictor_test_setup
from numpredict import NumPredictor

import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)

import pandas as pd
import unittest

class TestNumPredict(unittest.TestCase):
    def test_predict(self):
        pred = NumPredictor()
        result = pred.predict([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 5)
        result = [round(i) for i in result]

        expected_start = 21
        self.assertEqual(result[0], expected_start)

        for i, n in enumerate(result):
            if not i == 0:
                v = n - result[i-1]
                self.assertTrue(v == 2 or v == 3)

if __name__ == "__main__":
    unittest.main()