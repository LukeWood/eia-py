import os

from setuptools import find_packages
from setuptools import setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="eia-py-api",
    version=get_version("eia/__init__.py"),
    description="",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Luke Wood & others",
    author_email="lukewoodcs@gmail.com",
    url="https://github.com/lukewood/eia-py",
    license="Apache License 2.0",
    install_requires=[],
    extras_require={
        "dev": [
            "flake8",
            "black",
            "isort",
            "pytest",
            "pytype",
            "setuptools",
            "twine",
            "wheel",
            "sphinx-rtd-theme",
            "myst-parser",
            "sphinx-automodapi",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    packages=find_packages(),
)
