# -*- coding:utf-8 -*-

# TODO: 字典排序

from collections import OrderedDict


def dict_ordered():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    return d

d = dict_ordered()
import json
print(json.dumps(d))

