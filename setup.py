"""
Setup script for the kmsgrid module.
"""

import os
import subprocess
from setuptools import setup

import kmsgrid

def readme():
    """
    Return a properly formatted readme that is used as the long description for setuptools.setup.
    """
    with open('README.rst') as f:
        readme = f.read()
    return readme

setup(
    name='kmsgrid',
    version=kmsgrid.__version__,
    description='Read and convert grids from KMS.',
    long_description=readme(),
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: ISC License (ISCL)',
      'Topic :: Scientific/Engineering :: GIS',
      'Topic :: Utilities'
    ],
    entry_points = {
      'console_scripts': ['kmsgrid=kmsgrid:main']
    },
    keywords='kms geodesy grids geoid datumshift gridshift',
    url='https://github.com/Kortforsyningen/kmsgrid',
    author='Kristian Evers',
    author_email='kreve@sdfe.dk',
    license='ISC',
    py_modules=['kmsgrid'],
)
