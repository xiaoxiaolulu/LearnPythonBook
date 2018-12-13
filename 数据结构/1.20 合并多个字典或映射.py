# -*- coding: utf-8 -*-

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
