"""
pypredictor 0.1.0

© Hamd Waseem under the Apache Licence 2.0

_exceptions.py - exceptions
"""

class PyPredictorLengthOverflow(Exception): pass
class PyPredictorIncorrectColumns(Exception): pass

def exception(msg, type):
    raise type(msg)