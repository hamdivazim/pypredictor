"""
pypredictor 0.1.1

© Hamd Waseem under the Apache Licence 2.0

_exceptions.py - exceptions
"""

class PyPredictorLengthOverflow(Exception): pass
class PyPredictorIncorrectColumns(Exception): pass
class PyPredictorDataNotFound(Exception): pass
class PyPredictorInavlidDataType(Exception): pass

def exception(msg, type):
    raise type(msg)