#!/usr/bin/env python
__author__ = 'Albino'

import time


def computed_time(func):
    def wrapper(*args):
        time.clock()
        func(*args)
        print(time.clock())
    return wrapper