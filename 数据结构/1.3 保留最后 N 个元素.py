# -*- coding:utf-8 -*-

# TODO: 保留最后N个元素

from collections import deque


# def search(lines, pattern, history=5):
#
#     previous_lines = deque(maxlen=history)
#     for li in lines:
#         if pattern in li:
#             yield li, previous_lines
#         previous_lines.append(li)
#
#
# if __name__ == '__main__':
#
#     with open(r'G:\django-codes\LearnPythonBook\数据结构\test') as f:
#         for line, prevlines in search(f, 'python'):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-'*20)


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

# 使用deque(maxlen=N)构造函数会新建一个固定大小的队列 ，当新的元素加入并且这个队列已满时候，最老的元素会自动别移除掉
