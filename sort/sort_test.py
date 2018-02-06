#!/usr/bin/env python
__author__ = 'Albino'

import random
import time

from sort.insert_sort import insert_sort
from sort.selection_sort import selection_sort


def generate_list(n, l, r):
    return [random.randint(l, r) for x in range(n)]

if __name__ == '__main__':
    test_list = generate_list(1000, 1, 1000)
    # selection_sort(test_list)
    insert_sort(test_list)
