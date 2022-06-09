def dfs(start, end, graph, visited):
    if start == end:
        print(f'found {start}!')
        return True
    if start in visited:
        print(f'we"ve been here {start}')
        return False
    print(f'node {start}')
    visited += [start]
    for neighbour in graph[start]:
        if neighbour not in visited:
            if dfs(neighbour, end, graph, visited):
                return True
        print(f'we"ve been here neighbour {neighbour}')


graph = {
        '5': ['6', '7'],
        '6': ['10', '8'],
        '7': ['8', 'F'],
        '8': [],
        '9': ['F'],
        '10': ['5'],
    }
dfs('5', 'F', graph, [])
