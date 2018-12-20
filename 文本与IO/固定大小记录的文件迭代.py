# -*- coding:utf-8 -*-
from functools import partial

RECODE_SIZE = 32

with open('test.txt', 'rb') as f:

    records = iter(partial(f.read, RECODE_SIZE), b'')
    for item in records:
        print(item)