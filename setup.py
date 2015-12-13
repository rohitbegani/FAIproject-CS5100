# -*- coding: utf-8 -*-
"""Setup for dataset-examples."""
from setuptools import setup, find_packages

requires = [
        'pymongo',
        'numpy'
        ]

setup(
        name='User-Modelling',
        description='Modelling user preferences from DataSet.',
        author='Bhanu Jain, Rohit Begani, Ronny Mathew',
        homepage='http://github.com',
        packages=find_packages(),
        install_requires=requires,
        )

