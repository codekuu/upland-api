import setuptools
from os import path
from codecs import open

BASE = path.abspath(path.dirname(__file__))

with open(path.join(BASE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

about = {}
with open(path.join(BASE, "upland_api", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)  # nosec

setuptools.setup(
    name=about["__name__"],
    version=about["__version__"],
    packages=setuptools.find_packages(),
    install_requires=["requests==2.28.1", "pydantic==1.10.2"],
    python_requires=">=3.6",
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
