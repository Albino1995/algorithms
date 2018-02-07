#!/usr/bin/env python
__author__ = 'Albino'

import time


def computed_time(func, repeat=set()):
    def wrapper(*args, **kwargs):
        if func not in repeat:
            repeat.add(func)
            t0 = time.clock()
            result = func(*args, **kwargs)
            print(time.clock() - t0)
            # 拦截递归调用的函数后清空set
            repeat.remove(func)
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper