# -*- coding:utf-8 -*-

# TODO: 字符串的IO操作

import io
s = io.StringIO()
print(s.write('hello world'))
print(s.getvalue())
