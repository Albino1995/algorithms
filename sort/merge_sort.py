#!/usr/bin/env python
__author__ = 'Albino'

from sort.clock import computed_time


@computed_time
def MergeSort(list):
    """
    归并排序
    """
    if len(list) <= 1:
        return list
    mid = int(len(list) / 2)
    # 归并
    left = MergeSort(list[:mid])
    right = MergeSort(list[mid:])
    # 数组接近有序时的优化
    if left[-1] <= right[0]:
        return left + right
    return Merge(left, right)


def Merge(left, right):
    r, l = 0, 0
    result = []
    # 排序
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # left或者right索引指向末尾的时候与剩下的数合并
    result += left[l:]
    result += right[r:]
    return result
