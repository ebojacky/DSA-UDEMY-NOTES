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

    def bellman_ford(self, starting_node):
        # set distance to each node as infinity
        distances = { node: math.inf for node in self.graph_dict }
        paths = { node: "" for node in self.graph_dict }
        #paths_list_format = {node: [] for node in self.graph_dict}

        # set the starting node alone to zero
        distances[starting_node] = 0
        paths[starting_node] = starting_node
        #paths_list_format[starting_node] = [starting_node]

        # loop n -1 times
        length = len(self.graph_dict)
        print(length)
        for _ in range(length-1):
            print(_)
            #loop every edge : ie the starting point, destination and edge
            for node in self.graph_dict: # gets the nodes
                for child, weight in self.graph_dict[node].items(): #gets the edges
                    if distances[node] + weight < distances[child]:
                        distances[child] = distances[node] + weight
                        paths[child] = f"{paths[node]} -> {child}"
                        #paths_list_format[child] = paths_list_format[node] + [child]

        # check negative cycle
        for node in self.graph_dict:  # gets the nodes
            for child, weight in self.graph_dict[node].items():  # gets the edges
                if distances[node] + weight < distances[child]:
                    raise ValueError("Graph contains a negative-weight cycle")

        return distances,  paths

    def sssp_from_node(self, node):
        shortest_distance, shortest_path = my_graph.bellman_ford(node)
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