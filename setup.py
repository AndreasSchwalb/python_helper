#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='helper_python',
    version='0.0.2',
    description='Custom helper functions for python',
    author='Andreas Schwalb',
    author_email='andy@cyber-home.net',
    url='https://git.cyber-home.net/andy/helper_python.git',
    packages=find_packages(where='./src', include=('*')),
    package_dir={"": "src"},
    zip_safe=False
)
