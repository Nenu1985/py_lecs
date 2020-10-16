import sys
from collections import defaultdict

'''
8
54578972 99368556
79699669 54578972
64508306 99368556
56554555 64508306
27101564 81480071
89445516 27101564
93762227 81480071
89808815 93762227
4
56554555 2
93762227 79699669
99368556 2
64508306 56554555
27101564 2
99368556 79699669
93762227 2
56554555 54578972


10
85619126 64616465
98159933 85619126
73978229 85619126
29978081 64616465
72404745 29978081
97698445 75243921
36815728 97698445
18360411 97698445
66445821 75243921
92142380 66445821
4
97698445 4
75243921 92142380 98159933 73978229
66445821 4
29978081 92142380 73978229 97698445
18360411 4
29978081 92142380 98159933 97698445
36815728 4
64616465 92142380 97698445 29978081
'''
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

    import collections
    def bfs(graph, root): # breadth-first search
        visited, queue = set(), collections.deque([root])
        visited.add(root)
        while queue: 
            vertex = queue.popleft()
            for neighbour in graph[vertex]: 
                if neighbour not in visited: 
                    visited.add(neighbour) 
                    queue.append(neighbour)
        return visited

    clusters = []
    for query in queries:
        server_id_to_load = query['server_id_to_load']
        servers_from = query['server_ids_get_from']
        # check if servers in clusters
        server_cluster = [cluster for cluster in clusters if server_id_to_load in cluster]
        if not server_cluster:
            server_cluster = bfs(graph, server_id_to_load)
            clusters.append(server_cluster)

        else:
            server_cluster = server_cluster[0]
        

        # same_layer_servers = [server for server in server_cluster if server == server_id_to_load]

        to_download_from = [ser_id for ser_id in servers_from if ser_id in server_cluster]
        output += f'{len(to_download_from)} {" ".join(to_download_from)}\n'
    with open('output.txt', 'w') as f:
        f.write(output)
if __name__ == '__main__':
    main()