from setuptools import setup, find_packages

setup(
	name='furREST',
	version='0.1.0',
	description='A REST api wrapper for e621',
	author='0xyukine',
	packages=find_packages(),
	install_requires=[
	'requests',
	]
)