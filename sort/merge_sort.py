#!/usr/bin/env python
__author__ = 'Albino'

from sort.clock import computed_time


@computed_time
def MergeSort(list):
    if len(list) <= 1:
        return list
    num = int(len(list) / 2)
    left = MergeSort(list[:num])
    right = MergeSort(list[num:])
    return Merge(left, right)


def Merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result