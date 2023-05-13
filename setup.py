from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = 'The Python library that makes AI predictions simple.'
LONG_DESCRIPTION = """
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/hamdivazim/pypredictor/raw/main/logo_dark.png">
    <img src="https://github.com/hamdivazim/pypredictor/raw/main/logo.png" alt="pypredictor logo">
  </picture>
</div>

# pypredictor
<p>
  <img src="https://img.shields.io/badge/Python-3.8 | 3.9 | 3.10 | 3.11 -blue.svg" alt="py versions">
  <img src="https://img.shields.io/badge/PyPi package-0.1.0-green.svg" alt="pypi version">
  <img src="https://img.shields.io/badge/License-Apache License 2.0-green.svg" alt="license">
  <img src="https://img.shields.io/badge/Libraries-tensorflow | numpy | seaborn | pandas-green.svg" alt="libs">
</p>

The Python library that makes AI predictions simple.

### View the [GitHub Page](https://github.com/hamdivazim/pypredictor)

## What can it do?
pypredictor uses an RNN (Recurrent Neural Network) to predict the next n numbers in a sequence. As an example, using this code:
```python
pred = NumPredictor(500)
print(pred.predict([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 3))
```
pypredictor generated the following output, which is quite accurate:
```
[10.969043, 11.950292, 12.920968, 13.859894, 14.789316]
```
pypredictor also has the ability to generate a pandas DataFrame and a seaborn line graph, from an initial sequence/DataFrame which you provide.
###
Plus, there are examples in the `examples/` directory, so you can take a look for yourself :)

## How to install
Install via pip:
```
$ pip install pypredictor
```
To get examples, clone this repository and enter `pypredictor/examples`:
```
$ git clone https://github.com/hamdivazim/pypredictor.git
$ cd pypredictor/examples
```
anaconda support hopefully coming soon!

## License
pypredictor is licensed by Hamd Waseem (codingboy_CW) under [the Apache License 2.0](https://github.com/hamdivazim/pypredictor/blob/main/LICENSE).

"""

setup(
    name="pypredictor",
    version=VERSION,
    author="codingboy_CW (Hamd Waseem)",
    author_email="codingboy.cw@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['tensorflow', 'pandas', 'numpy', 'matplotlib', 'seaborn'],
    keywords=['python', 'prediction', 'ai'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: Apache Software License"
    ],
    license="Apache-2.0"
)