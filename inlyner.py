#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2019 Ghostkeeper
# This package is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This package is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

def inlyner(func):
	"""
	Inlines function calls inside this function in an attempt to improve
	performance.
	:param func: The function to inline.
	:return: A transformed function with some subcalls inside it inlined.
	"""
	#TODO: Inline subcalls inside this function.
	return func

class Inlyner(type):
	"""
	This is a metaclass that attempts to inline function calls for better
	performance.
	"""

	def __new__(typ, name, bases, clsdict):
		"""
		Inline function calls within this class in an attempt to improve
		performance.
		:param name: The name of the class.
		:param bases: The base classes that this class depends on, in the MRO.
		:param clsdict: All members of the class.
		:return: A modified class where some of the methods have their function
		calls inlined.
		"""
		for key, value in clsdict.items():
			if callable(value):
				clsdict[key] = inlyner(value)
		return super().__new__(typ, name, bases, clsdict)