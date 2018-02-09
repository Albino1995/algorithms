#!/usr/bin/env python
__author__ = 'Albino'

import random

from sort.insertion_sort import InsertionSort
from sort.selection_sort import SelectionSort
from sort.bubble_sort import BubbleSort
from sort.merge_sort import MergeSort
from sort.quick_sort import QuickSort


def generate_list(n, l, r):
    return [random.randint(l, r) for x in range(n)]


if __name__ == '__main__':
    test_list = generate_list(5000, 1, 5000)
    # SelectionSort(test_list)
    # InsertionSort(test_list)
    # BubbleSort(test_list)
    # MergeSort(test_list)
    QuickSort(test_list, 0, len(test_list) - 1)