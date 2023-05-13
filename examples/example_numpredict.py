"""
pypredictor 0.1.1

© Hamd Waseem under the Apache Licence 2.0

example_numpredict.py - example usage of NumPredictor
"""

from pypredictor import numpredict # Import the necessary library

pred = numpredict.NumPredictor()
"""
 _________________________________
|                                 |
|  Initialisation of NumPredictor |
|_________________________________|

This is essentially just the creation of a 'model'. It contains the necessary methods to predict next values in a sequence.

By default, NumPredictor uses 500 epochs as this is what I have found to be quite accurate with SMALL datasets.
However, depending on the size of your dataset, you may want to change the amount of epochs. You can do this by:
```
pred = numpredict.NumPredictor(200)
                                ^
                         amount of epochs
```
To change it later, you can also use the `set_accuracy()` method.
"""

dataset = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = pred.predict(dataset, 5, 8)
print(result)
"""
 _________________________
|                         |
|     Predicting Data     |
|_________________________|

Now using NumPredictor, we can predict the next n numbers in a sequence using the `predict` method.
There are three key parameters:
    -  sequence
    -  n
    -  n_steps (by default set to 5)

`sequence` is the list you give to be analysed. It should be a list of numbers.
`n` is the amount of values you want predicted. In the example above, n is set to 5, so we expect 5 elements generated and returned back.
`n_steps` defines how many elements should be looked into. In the above example, n_steps is 8, so it will analyse the last 8 elements and make prediction based off of that.

In the example above, we expect the output to be close to [110, 120, 130, 140, 150] as this is the general trend.
"""

