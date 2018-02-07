#!/usr/bin/env python
__author__ = 'Albino'

from .clock import computed_time


@computed_time
def selection_sort(list):
    """
    选择排序
    """
    for i in range(len(list)):
        # 寻找[i, n)区间的最小值
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        # 交换
        list[i], list[min_index] = list[min_index], list[i]
    return list
