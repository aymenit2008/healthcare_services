# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in healthcare_services/__init__.py
from healthcare_services import __version__ as version

setup(
	name='healthcare_services',
	version=version,
	description='Healthcare Services',
	author='Yamaan org',
	author_email='aymen.alsurabi@yamaan.org',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
