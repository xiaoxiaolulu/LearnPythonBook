# -*- coding:utf-8 -*-

# TODO: 删除序列相同的元素并保持顺序


# def dedupe(items):
#
#     seen = set()
#
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
# a = [1, 3, 1, 2, 1, 4]
# print(list(dedupe(a)))


def dedupe(items, key=None):

    seen = set()

    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
