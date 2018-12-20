# -*- coding:utf-8 -*-

import gzip
# with gzip.open(r'G:\django-codes\LearnPythonBook\文本与IO\test.gz', 'wt') as f:
#     text = f.write('hahahhaha')

with gzip.open(r'G:\django-codes\LearnPythonBook\文本与IO\test.gz', 'rt') as f:
    text = f.read()
    print(text)
