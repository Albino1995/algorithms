#!/usr/bin/env python
__author__ = 'Albino'

import time


def BinarySearch(list, n, target):
    """
    迭代版本二分查找
    找到target,则返回索引，否则返回-1
    """
    l, r = 0, n - 1
    while l <= r:
        mid  = (l + r) // 2
        if list[mid] == target:
            return mid
        elif target < list[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return -1


def BinarySearch2(list, l, r, target):
    """
    递归版本二分查找
    找到target,则返回索引，否则返回-1
    """
    mid = (l + r) // 2
    if l > r:
        return -1

    if list[mid] == target:
        return mid
    elif list[mid] > target:
        return BinarySearch2(list, l, mid - 1, target)
    else:
        return BinarySearch2(list, mid + 1, r, target)


if __name__ == '__main__':
    test_list = list(range(100))
    # t0 = time.clock()
    for i in test_list:
        print(BinarySearch2(test_list, 0, len(test_list) - 1, i))
    # t1 = time.clock() - t0
    # print(t1)