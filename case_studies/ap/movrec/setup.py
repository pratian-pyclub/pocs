# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='movrec',
    version='0.0.1',
    description='Accurate Movie Recommendations using Collaborative Filtering',
    long_description=readme,
    author='Swaathi Kakarla',
    author_email='swaathi@skcript.com',
    url = 'https://github.com/skcript/movrec',
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'movrec': ['data/*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'movrec = movrec.cli:main',
        ],
    },
    install_requires=(
    	['click', 'pandas', 'numpy', 'scikit-learn']
    )
)
