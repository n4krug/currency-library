from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A module for interfacing with the OpenExchangeRates API'
LONG_DESCRIPTION = 'A package that allows you to interface with the OpenExchangeRates.com API to get current rates and convert between currencies.'

# Setting up
setup(
    name="oer-api",
    version=VERSION,
    author="n4kruG (Gustav Eneberg)",
    author_email="<gustav.eneberg@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'money', 'currency', 'currencies', 'currency converter', 'api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)