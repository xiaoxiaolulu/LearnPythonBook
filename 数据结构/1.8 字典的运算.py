# -*- coding:utf-8 -*-

# TODO: 字典的运算

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

minx = min(zip(prices.values(), prices.keys()))
print(minx)

prices_stored = sorted(zip(prices.values(), prices.keys()))
print(prices_stored)

print(list(zip(prices.values(), prices.keys())))
