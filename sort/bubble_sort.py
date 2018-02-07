#!/usr/bin/env python
__author__ = 'Albino'

from sort.clock import computed_time


@computed_time
def BubbleSort(list):
    for i in range(len(list) - 1):
        # 内层循环中后i个数已经有序
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
