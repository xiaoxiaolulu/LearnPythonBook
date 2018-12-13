# -*- coding:utf-8 -*-
"""
任何序列（迭代对象) 可以通过一个简单的赋值语句解压给多个变量

唯一的前提就是变量的数量必须跟序列的元素数量一样多
"""

# data = ['ACME', 50, 91.1, (2012, 12, 21)]
#
# name, shares, price, date = data
#
# print(name)
# print(shares)
# print(price)
# print(date)


"""
赋值变量数量与序列中元素数量不一致, 抛出异常ValueError
"""

# data_test = [1, 2, 3]
# a, b, c, d = data_test

# ValueError:需要解压的值太多(预期2)
# ValueError: not enough values to unpack (expected 4, got 3)
# print(a)

"""
这种解压赋值可以用于任何可迭代的对象

列表、元祖、字符串、文件对象、迭代器、生成器
"""

# z = 'hello'
#
# v, n, m, o, p = z
# print(v, n, m, o, p)

# 如果只想解压一部分，丢弃其他的值， 对于这种情况
# 可以使用任意变量名去占位，再丢弃这些变量就行

ex = 'world'
# 只想取O
_, b, _, _, _ = ex
print(b)

'''必须保证这些丢弃的 变量名没有地方用'''
