#!/usr/bin/env python3

from setuptools import setup

setup(
    name='roo',
    version='0.1',
    py_modules=['roocli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        roo=roocli:cli
    ''',
)
