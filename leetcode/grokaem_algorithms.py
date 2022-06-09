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

from collections import deque
# have a graph
# 5: 6,7
# 6: F,8
# 7: 8, 9
# 8: 
# 9: F
def bfs_canonical():

    print('Breadth First Search started')
    graph = {}
    graph['5'] = ['6', '7']
    graph['6'] = ['F', '8']
    graph['7'] = ['8', '9']
    graph['8'] = []
    graph['9'] = ['F']

    search_queue = deque()
    search_queue += graph['5']

    searched = []
    while search_queue:
        nodes = search_queue.popleft()
        
        for node in nodes:
            if node not in searched:
                if node == 'F':
                    print(f'We"ve found F in node {node}!')
                    return True
                else:
                    print(f'node {node} is not F. Adding {graph[node]} to a queue')
                    search_queue += graph[node]
        print(f'node {node} has checked')
        search_queue.append(node)
    print('No F has found')
    return False

bfs_canonical()