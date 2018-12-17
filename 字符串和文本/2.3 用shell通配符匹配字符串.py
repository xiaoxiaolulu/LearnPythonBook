# -*- coding:utf-8 -*-

# TODO: 用shell通配符匹配字符串
from fnmatch import fnmatch, fnmatchcase

print(fnmatch(r'test.yaml', '*.yaml'))
