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