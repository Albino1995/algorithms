#!/usr/bin/env python
__author__ = 'Albino'

import heapq

from sort.clock import computed_time


@computed_time
def HeapSort(list):
    heapq.heapify(list)
    return heapq.nlargest(len(list), list)
