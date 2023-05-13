from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'A Python library that can predict the next values in a list.'
LONG_DESCRIPTION = 'A Python library that can predict the next values in a list. (long desc here)'

# Setting up
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