#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pelican.bitly',
    version='0.1',
    description='Plugin for pelican to add bit.ly short urls '
                'to pages and articles. Useful for analytics of retweet',
    author='Rach Belaid',
    author_email='dev@ironbraces.com',
    url='https://github.com/rach/pelican.bitly',
    packages=find_packages(),
    install_requires=[
        'pelican>=3.0',
        'bitlyapi',
    ],
    )
