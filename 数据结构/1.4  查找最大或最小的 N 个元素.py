# -*- coding:utf-8 -*-

# TODO 查找最大或最小的N个元素
import heapq


nums = [1, 2, 54, 4, 32, 1000, 99, 32]

maxx = heapq.nlargest(3, nums)
print(maxx)

minx = heapq.nsmallest(3, nums)
print(minx)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AA', 'shares': 50, 'price': 92.1},
    {'name': 'FM', 'shares': 10, 'price': 22.1}
]

print(heapq.nsmallest(1, portfolio, key=lambda s: s['price']))
print(heapq.nlargest(1, portfolio, key=lambda s: s['price']))


n = [1, 78, 22, 32, 3333, 222, 12, 323]
import heapq
heapq.heapify(n)
print(n)
print(heapq.heappop(n))
print(heapq.heappop(n))
print(heapq.heappop(n))