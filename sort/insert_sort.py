#!/usr/bin/env python
__author__ = 'Albino'

from .clock import computed_time


@computed_time
def insert_sort(list):
    """
    插入排序
    """
    for i in range(1, len(list)):
        # 寻找list[i]合适的插入位置, 第一个元素默认排好序
        j = i
        while j > 0:
            if list[j] < list[j-1]:
                list[j-1], list[j] = list[j], list[j-1]
            else:
                break
            j -= 1

    return list