# -*- coding:utf-8 -*-

import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):

    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


size = 10000000
with open('hello', 'wb') as f:
    f.seek(size-1)
    f.write(b'xoooo')