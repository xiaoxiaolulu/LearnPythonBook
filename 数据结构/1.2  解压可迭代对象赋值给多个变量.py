# -*- coding:utf-8 -*-

# TODO:  解压可迭代对象赋值给多个变量

"""
如果赋值的数量超过迭代对象超过的变量个数时，会抛出哪一个ValueError
如果从迭代对象中解压N个元素来?
"""

# r = (1, 2, 3, 4, 5, 6, 7, 8)
# a, b, *args = r
# print(a)
# print(b)
# print(args)

# 解压出的args永远是List类型

line = r"G:/django-codes/LearnPythonBook"

z, *args, v = line.split(":")
print(line.split(":"))
print(z)
print(*args)
print(v)
