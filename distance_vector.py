def distance_vector_algorithm(graph):

    distance_vectors = {node: {neighbor: float('inf') for neighbor in graph} for node in graph}
    
    # Set distance to self as 0
    for node in graph:
        distance_vectors[node][node] = 0
        for neighbor, weight in graph[node].items():
            distance_vectors[node][neighbor] = weight

    # Run the Distance Vector Algorithm
    changed = True
    while changed:
        changed = False
        for node in graph:
            for neighbor in graph[node]:
                for dest in distance_vectors[neighbor]:
                    if distance_vectors[node][dest] > distance_vectors[node][neighbor] + distance_vectors[neighbor][dest]:
                        distance_vectors[node][dest] = distance_vectors[node][neighbor] + distance_vectors[neighbor][dest]
                        changed = True

    return distance_vectors


# Example graph (adjacency list)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'D': 3},
    'D': {'B': 2, 'C': 3}
}

distance_vectors = distance_vector_algorithm(graph)

for node, vector in distance_vectors.items():
    print(f"Distance vector for {node}:")
    for dest, cost in vector.items():
        print(f"  To {dest}: {cost}")
