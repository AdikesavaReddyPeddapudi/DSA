import heapq

def dijkstra(graph, source):
    # Initialize distances
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

result = dijkstra(graph, 'A')
print(result)

print("Shortest distances from A:")
for node in result:
    print(f"A → {node} = {result[node]}")