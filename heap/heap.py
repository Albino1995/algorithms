#!/usr/bin/env python
__author__ = 'Albino'

import heapq
import random

test_list = list(random.sample(range(100), 10))
print('original list is', test_list)
heapq.heapify(test_list)
k = 3
largest = heapq.nlargest(k, test_list)
smallest = heapq.nsmallest(k, test_list)
print('heap is', test_list)
heapq.heappush(test_list, 20)
print('heap is', test_list)
print('largest-' + str(k), '  is ', largest)
print('smallest-' + str(k), ' is ', smallest)

