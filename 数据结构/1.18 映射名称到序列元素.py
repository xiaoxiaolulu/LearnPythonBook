# -*- coding:utf-8 -*-

# TODO: 映射名称到序列元素

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(Subscriber)
print(sub)

Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.addr)
print(sub.joined)