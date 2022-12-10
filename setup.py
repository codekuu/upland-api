import setuptools
from os import path
from upland_api.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __name__,
    __url__,
    __version__,
)

BASE = path.abspath(path.dirname(__file__))

with open(path.join(BASE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name=__name__,
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=["requests==2.28.1", "pydantic==1.10.2"],
    python_requires=">=3.6",
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
