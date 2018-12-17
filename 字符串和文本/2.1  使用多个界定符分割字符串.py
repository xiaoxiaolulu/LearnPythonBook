# -*- coding:utf-8 -*-

# TODO: 使用多个界定符分割字符串

line = 'asdf fjdk; afed, fjek,asdf, foo'

import re

print(re.split(r'[;,\s]\s*', line))
