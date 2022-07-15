# -*- coding: utf-8 -*-

from  typing_extensions.version import __version__
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

# usage:
# python setup.py bdist_wininst generate a window executable file
# python setup.py bdist_egg generate a egg file
# Release information about eway

version = __version__
name = "typing_extensions"
description = "clone typing_extensions from https://github.com/python/typing_extensions"
author = "yumoqing"
email = "yumoqing@gmail.com"

package_data = {}

setup(
	name="typing_extensions",
	version=version,
	
	# uncomment the following lines if you fill them out in release.py
	description=description,
	author=author,
	author_email=email,
   	platforms='any',
	install_requires=[
	],
	packages=[
		"typing_extensions"
	],
	package_data=package_data,
	keywords = [
	],
	url="https://github.com/yumoqing/typing_extensions",
	long_description=description,
	long_description_content_type="text/markdown",
	classifiers = [
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
	],
)
