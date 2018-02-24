#!/usr/bin/env python
__author__ = 'Albino'

from sort.clock import computed_time


@computed_time
def QuickSort3Ways(list, l, r):
    if l >= r:
        return list
    # 标定点
    key = list[l]
    # list[l+1...lt] < key
    lt = l
    # list[gt...r] > key
    gt = r + 1
    # list[lt+1...i) == key
    i = l + 1
    while i < gt:
        if list[i] < key:
            list[i], list[lt+1] = list[lt+1], list[i]
            lt += 1
            i += 1
        elif list[i] > key:
            list[i], list[gt-1] = list[gt-1], list[i]
            gt -= 1
        else:
            i += 1

    list[l], list[lt] = list[lt], list[l]
    QuickSort3Ways(list, l, lt - 1)
    QuickSort3Ways(list, gt, r)
    return list