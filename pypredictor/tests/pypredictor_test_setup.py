"""
pypredictor 0.1.1

© Hamd Waseem under the Apache Licence 2.0

pypredictor_test_setup.py - test setup to allow access to previous directory
"""

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(parent_dir)