# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='grains-image-classification',
    version='0.1.2',
    description='Identify a grain with ML',
    long_description=readme,
    author=['Swaathi Kakarla'],
    author_email='swaathi@skcript.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=(
    	['pillow'], ['pybrain'], ['scipy']
    )
)
