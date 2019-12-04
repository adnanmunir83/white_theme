# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in white_theme/__init__.py
from white_theme import __version__ as version

setup(
	name='white_theme',
	version=version,
	description='White Theme',
	author='RF',
	author_email='rf@rf.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
