from setuptools import setup, find_packages

setup(
	name='furREST',
	version='0.1.1',
	description='A REST api wrapper for e621',
	author='0xyukine',
	license='Apache-2.0',
	package_dir={'':'src'},
	packages=find_packages(where='src'),
	install_requires=['requests'],
	zip_safe=False
)