import sys
from collections import defaultdict

def get_input_data(file):
    server_pairs = []
    # file case:
    with open(file, 'r') as file:
        lines = file.readlines()
        N = int(lines[0])  # number of connections
        server_pairs = [pair.strip().split() for pair in lines[1:N+1]]

        
        Q = int(lines[N+1])
        queries = []
        # queries = [server_id.strip().split()[0] for server_id in lines[N+2:]]
        for i in range(Q):
            server_id = lines[N + 2 + i*2].split()[0]
            server_ids_which_contain_file = lines[N + 2 + i*2 + 1].split()
            queries.append({
                'server_id_to_load': server_id,
                # 'num_of_servers': int(num_of_servers_to_load),
                'server_ids_get_from': server_ids_which_contain_file,
            })
            
    graph = defaultdict(set, {})
    # [for pair in server_pairs]
    for pair in server_pairs:
        graph[pair[0]].add(pair[1])
        graph[pair[1]].add(pair[0])
        
    return graph, queries


def main():
    graph, queries = get_input_data(file='input.txt')
    output = ''

    visited = {key:False for key in graph.keys()}
    component = {key:-1 for key in graph.keys()}  # для каждой вершины храним номер её компоненты
    num_components = 0

    def dfs(node):  # depth-first search
        component[node] = num_components
        visited[node] = True
        for w in graph[node]:
            if visited[w] == False:
                dfs(w)

    for node_num in graph.keys():
        if not visited[node_num]:
            dfs(node_num)
            num_components += 1

    for query in queries:
        server_id_to_load = query['server_id_to_load']
        servers_from = query['server_ids_get_from']
        num_of_claster = component[server_id_to_load]
        same_layer_servers = [t for t, v in component.items() if v == num_of_claster]

        to_download_from = [ser_id for ser_id in servers_from if ser_id in same_layer_servers]
        output += f'{len(to_download_from)} {" ".join(to_download_from)}\n'
    with open('output.txt', 'w') as f:
        f.write(output)
if __name__ == '__main__':
    main()