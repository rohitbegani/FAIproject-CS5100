# -*- coding: utf-8 -*-
"""Setup for user modelling project."""
from setuptools import setup, find_packages

requires = [
        'pymongo',
        'plotly'
        ]

setup(
        name='User Based Recommendation System',
        description='Model user preferences to provide Location Based Recommendation.',
        author='Bhanu Jain, Rohit Begani, Ronny Mathew',
        url='http://rohitbegani.github.io/FAIproject-CS5100',
        packages=find_packages(),
        install_requires=requires,
        )

