def dfs(graph,node,visited):
    visited.add(node)
    print(node,end=' ')

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)

graph={
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': [ ]
}
visited = set()
dfs(graph,'A',visited)