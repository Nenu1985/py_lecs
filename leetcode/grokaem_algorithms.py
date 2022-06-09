def recursion_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    return arr[0] + recursion_sum(arr[1:])

print(recursion_sum([2,3,5,6]))


from collections import defaultdict
from itertools import count
import queue
from timeit import default_timer
from typing import DefaultDict


def sum_recursion(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    return arr[0] + sum_recursion(arr[1:])


print(sum_recursion([1,2,3]))

def count_recursion(arr):
    if len(arr) == 0:
        return 0
    return 1 + count_recursion(arr[1:])

print(count_recursion([1,2,3]))


def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    lesser = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return qsort(lesser) + [pivot] + qsort(greater)


print(qsort([3,4,6,34,2,2,141,44,23]))

