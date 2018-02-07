#!/usr/bin/env python
__author__ = 'Albino'

from sort.clock import computed_time


@computed_time
def InsertionSort(list):
    """
    插入排序
    """
    for i in range(1, len(list)):
        # 待插入的元素
        e = list[i]
        # e应该插入的位置
        j = i
        while j > 0 and list[j-1] > e:
            list[j] = list[j-1]
            j -= 1
        list[j] = e

    return list