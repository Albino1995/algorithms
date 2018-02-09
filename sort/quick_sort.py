#!/usr/bin/env python
__author__ = 'Albino'

from sort.clock import computed_time


@computed_time
def QuickSort(list, low, high):
    # i指向第一个元素
    i = low
    # j指向最后一个元素
    j = high
    if i >= j:
        return list
    key = list[i]
    while i < j:
        while i < j and list[j] >= key:
            j = j - 1
        list[i] = list[j]
        while i < j and list[i] <= key:
            i = i + 1
        list[j] = list[i]
    list[i] = key
    QuickSort(list, low, i-1)
    QuickSort(list, j+1, high)
    return list