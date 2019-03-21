#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='bing-search',
    version='1.0.0',
    description='Bing Search',
    long_description='Python command line appliation to search on bing.com and return urls in the search results',
    keywords='bing search',
    author='Dheeraj',
    author_email='dheer047@gmail.com',
    maintainer='Dheeraj',
    maintainer_email='dheer047@gmail.com',
    url='https://github.com/dheeraj-rn/bing-search',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bing = scripts.bing:main',
        ]
    },
    install_requires=[
        'requests',
    ]
)
