# -*- coding:utf-8 -*-

import os.path


def read_into_buffer(filename):

    buf = bytearray(os.path.getsize(filename))

    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


b = read_into_buffer('hello')
print(b)
