def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            vertex = int(parts[0])
            neighbors = list(map(int, parts[1].strip().split(',')))
            graph[vertex] = neighbors
    return graph

def dfs(graph, start, visited, target):
    visited[start] = True
    for neighbor in graph.get(start, []):
        if not visited[neighbor] and neighbor != target:
            dfs(graph, neighbor, visited, target)

def find_root_vertex(graph):
    vertices = list(graph.keys())
    for vertex in vertices:
        visited = {v: False for v in vertices}
        dfs(graph, vertex, visited, vertex)
        if all(visited.values()):
            return vertex
    return -1

def write_result_to_file(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    graph = read_graph_from_file('input.txt')
    root_vertex = find_root_vertex(graph)
    write_result_to_file('output.txt', root_vertex)
