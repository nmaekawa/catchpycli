#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

import os
import re
import codecs


def read_version():
    version_file = codecs.open(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                'catchpycli/__init__.py'),
            'r', 'utf-8').read()
    return re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]",
            version_file, re.M).group(1)

version = read_version()

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
    "requests",
]

test_requirements = [
    "pytest",
    "httpretty",
    "sure"
]

setup(
    name='catchpycli',
    version='0.1.0',
    description="python  client library for catchpy rest api",
    long_description=readme,
    author="nmaekawa",
    author_email='nmaekawa@g.harvard.edu',
    url='https://github.com/nmaekawa/catchpycli',
    packages=find_packages(exclude=["docs", "tests*"]),
    package_dir={'catchpycli':
                 'catchpycli'},
    entry_points={
        'console_scripts': [
            'catchpycli=catchpycli.cli:main'
        ]
    },
    include_package_data=True,
    license="Apache Software License 2.0",
    keywords='catchpycli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
)
