import heapq
import math


class Weighted_Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_node(self, value):
        if value not in self.graph_dict:
            self.graph_dict[value] = {}

    def add_edge(self, node, edge, weight):
        if edge not in self.graph_dict[node]:
            self.graph_dict[node].update({edge: weight})

    def __str__(self):
        string = ""
        for node in self.graph_dict:
            string += f"{node}: {self.graph_dict[node]}\n"
        return string

    def dijkstra(self, starting_node):
        # set distance to each node as infinity
        distances = {node: math.inf for node in self.graph_dict}
        paths = {node: "" for node in self.graph_dict}

        # set the starting node alone to zero
        distances[starting_node] = 0
        paths[starting_node] = starting_node

        # create a queue as a todo list for the nodes to be visited
        # the queue tracks the distance and path
        queue = [(0, starting_node, starting_node)]

        while queue:
            distance, node, path = heapq.heappop(queue) # get the shortest distance in queue

            if distance > distances[node]:
                continue

            for child, weight in self.graph_dict[node].items():
                distance_path = distance + weight
                new_path = f"{path} -> {child}"
                if distance_path < distances[child]:
                    distances[child] = distance_path
                    paths[child] = new_path
                    heapq.heappush(queue,(distance_path, child, new_path))

        return distances,  paths

    def sssp_from_node(self, node):
        shortest_distance, shortest_path = my_graph.dijkstra(node)
        print(f"Shortest Distance to all nodes from {node}: \n {shortest_distance}")
        print(f"Shortest PATH to all nodes from {node}: \n {shortest_path}")


graph_dict = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

my_graph = Weighted_Graph(graph_dict=graph_dict)
print(my_graph)
my_graph.add_node("G")
my_graph.add_edge("A", "G", 10)
my_graph.add_edge("G", "F", 11)
print(my_graph)
my_graph.sssp_from_node("A")