# Initialize the adjacency matrix with weights
graph = [[0, 5, float('inf'), 10],
         [float('inf'), 0, 3, float('inf')],
         [float('inf'), float('inf'), 0, 1],
         [float('inf'), float('inf'), float('inf'), 0]]

# Apply the Floyd-Warshall algorithm
for k in range(len(graph)):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# Print the resulting shortest path distances
for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j], end='\t')
    print()

print(len(graph))