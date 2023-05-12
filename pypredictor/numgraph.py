"""
pypredictor 0.1.0

© Hamd Waseem under the Apache Licence 2.0

numgraph.py - Using `NumPredictor`, generates a seaborn plot.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpredict
import _exceptions

class NumGraph:
    """ Base class for generating seaborn plots. """

    def __init__(self, data=[]):
        self.set_data(data)

    def to_dataframe(self):
        """ Generates a `pd.DataFrame` from inputted data. """
        if len(self.data) < 1:
            _exceptions.exception("Data for NumGraph not given. Use `set_data()`.", _exceptions.PyPredictorDataNotFound)

        return pd.DataFrame({"data": self.data})
    
    def set_data(self, data: list):
        """ Sets data. """

        if not all(isinstance(element, (int, float)) for element in data):
            _exceptions.exception("All elements in the sequence must be numbers.", _exceptions.PyPredictorInavlidDataType)

        self.data = data
        self.generated = []

    def get_normal_plot(self, _df="nmdf"):
        """ Gets seaborn plot for given data. """
        df = self.to_dataframe() if _df == "nmdf" else _df

        plot = sns.catplot(x=df.index, y='data', data=df, kind='point')

        plt.title('')

        plt.xlabel('')
        plt.ylabel('')

        return plot
    
    def predict(self, n, n_steps=5):
        """ Predicts based on given data and returns a catplot with new data. """

        pred = numpredict.NumPredictor()
        results = pred.predict(pred, n, n_steps)
        
        self.generated = results

        df = pd.DataFrame({"data":results})

        return self.get_normal_plot(df)
    