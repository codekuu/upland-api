import setuptools
from os import path


BASE = path.abspath(path.dirname(__file__))

with open(path.join(BASE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="upland-developers-api",
    version="1.0.0",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
    author="Kevin Kuusela",
    author_email="kevin@oppetinternet.se",
    description="Upland Developers API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codekuu/upland-api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)