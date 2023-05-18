"""
pypredictor 0.1.1

© Hamd Waseem under the Apache Licence 2.0

numpredict.py - Predicts the next n numbers in a list.
"""

import logging
import numpy as np
import pandas as pd
from . import _exceptions
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

class NumPredictor:
    """ Base NumPredictor class that generates the next values in a list. """

    def __init__(self, epochs=500):
        self.epochs = epochs
        self.tf_verbose = True
        self.set_verbose(self.tf_verbose)

    def set_verbose(self, verbose=True):
        """ Gives option to suppress tensorflow's info output. """
        self.tf_verbose = verbose

        if self.tf_verbose:
            logging.getLogger('tensorflow').setLevel(logging.INFO)
        else:
            logging.getLogger('tensorflow').setLevel(logging.ERROR)

    def _prepare_data(self, sequence, n_steps):
        """ Prepare the data for training the RNN """
        x, y = [], []

        for i in range(len(sequence)):
            # Find the end of the input sequence
            end_ix = i + n_steps
            if end_ix > len(sequence) - 1:
                break

            # Separate input and output parts of the pattern
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            x.append(seq_x)
            y.append(seq_y)

        return np.array(x), np.array(y)
    
    def set_accuracy(self, new):
        """ Sets amount of epochs to be used """
        self.epochs = new

def predict(self, sequence: list, n: int, n_steps=5):
    """ Predicts the next n elements in the provided list. """

    if n_steps >= len(sequence):
        _exceptions.exception(f"Inavlid n_steps value ({n_steps}). Cannot be equal to or more than sequence length.", _exceptions.PyPredictorLengthOverflow)
    elif n_steps <= 0:
        _exceptions.exception(f"Inavlid n_steps value ({n_steps}). Cannot be zero or negative.", _exceptions.PyPredictorLengthOverflow)
    
    if not all(isinstance(element, (int, float)) for element in sequence):
        _exceptions.exception("All elements in the sequence must be numbers.", _exceptions.PyPredictorInavlidDataType)

    x, y = self._prepare_data(sequence, n_steps)

    # Reshape the input data for the LSTM model (samples, time steps, features)
    n_samples = x.shape[0]
    n_features = 1
    x = x.reshape((n_samples, n_steps, n_features))

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    # Train the model
    model.fit(x, y, epochs=self.epochs, verbose=0)

    # Generate the next n numbers
    last_sequence = sequence[-n_steps:]
    generated = []
    for _ in range(n):
        x = np.array(last_sequence[-n_steps:]).reshape((1, n_steps, n_features))
        pred = model.predict(x)[0][0]

        if all(isinstance(element, int) for element in sequence):
            # If original values were integers, round the prediction
            pred = round(pred)

        generated.append(pred)
        last_sequence.append(pred)

    return generated

    
    def predict_dataframe(self, df: pd.DataFrame, column: str, n: int, n_steps=5):
        if  df.shape[1] != 1:
            _exceptions.exception("DataFrame must only have 1 column.", _exceptions.PyPredictorIncorrectColumns)

        sequence = df[column].tolist()

        df[column] = self.predict(sequence, n, n_steps)

        return df
