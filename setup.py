from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in corecentric/__init__.py
from corecentric import __version__ as version

setup(
	name='corecentric',
	version=version,
	description='Stock Module',
	author='Corecentric',
	author_email='corecentric@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
