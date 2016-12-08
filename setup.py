#!/usr/bin/env python3

from distutils.core import setup
from setuptools import find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Python MMorph Library',
    version='0.1.0',
    author='Felipe Anchieta Santos Costa',
    author_email='felipe.anchieta@aluno.ufabc.edu.br',
    url='http://bcc.ufabc.edu.br',
    packages=find_packages()
)
