# -*- coding:utf-8 -*-

# TODO: 字典中的键映射多个值

d = {
    'a': [1, 2, 3]
}

from collections import defaultdict

dw = defaultdict(list)
dw['a'].append(1)
dw['a'].append(2)
dw['b'].append(4)

print(dw)

dc = defaultdict(set)
dc['a'].add(1)
dc['a'].add(2)
dc['b'].add(3)

print(dc)

# defaultdict 会自动为将要访问的键创建映射实体

ws = {}
ws.setdefault('a', []).append(1)
ws.setdefault('b', []).append(2)

print(ws)
