"""Package setup"""
from setuptools import setup, find_packages


with open("blokus/version.py") as f:
    __version__ = ""
    exec(f.read(), globals())  # pylint: disable=exec-used


with open("README.md") as f:
    README = f.read()

setup(
    name="blokus",
    version=__version__,
    description="Python implementation of the Blokus board game.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jason-ash/blokus",
    author="Jason Ash",
    author_email="ash.jasont@gmail.com",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": [
            "black==20.8b1",
            "pre-commit==2.9.3",
            "pylint==2.6.0",
            "mypy==0.790",
        ]
    },
    include_package_data=True,
    package_data={"blokus": ["../README.md", "../LICENSE.md", "../MANIFEST.in"]},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite="tests",
    zip_safe=False,
)
