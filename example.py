#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2019 Ghostkeeper
# This package is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This package is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

"""
Example usage of Inlyner.
"""

import inlyner

@inlyner.inlyner
def func():
	x = twice(5) + twice(6)
	return x

def twice(num):
	return num * 2