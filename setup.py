#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='BingSearchCli',
    version='0.1.0',
    description='Bing Search Cli',
    long_description='python command line appliation to search on bing.com and return urls in the search results',
    keywords='bing search cli',
    author='Dheeraj',
    author_email='dheer047@gmail.com',
    maintainer='Dheeraj',
    maintainer_email='dheer047@gmail.com',
    url='https://github.com/dheeraj-rn/BingSearchCli',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bingsearchcli = scripts.bingsearchcli:main',
        ]
    },
    install_requires=[
        'requests',
    ]
)
