# -*- coding: utf-8 -*-

#  TODO: 命名切片

record = '....................100 .......513.25 ..........'

# cost = int(record[20:23])*float(record[31:37])
# print(cost)

SH = slice(20, 23)
PR = slice(31, 37)
cost = int(record[SH])*float(record[PR])
print(cost)
