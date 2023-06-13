from collections import deque


class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.adjacency_dict = graph_dict

    def __str__(self):
        string = ""
        for v in self.adjacency_dict:
            string += f"{v}: {self.adjacency_dict[v]}\n"
        return string

    def bfs_for_sssp(self, starting_vertex, ending_vertex):

        queue = deque()  # queue of all the unique path
        queue.append([starting_vertex])

        while queue:
            current_path = queue.popleft()
            current_vertex = current_path[-1]

            if current_vertex == ending_vertex:
                return current_path

            # get the edges of the current_vertex. if current vertex has no list, return []
            for edge in self.adjacency_dict.get(current_vertex, []):
                new_path = list(current_path)  # create a unique new path
                new_path.append(edge)
                queue.append(new_path)


graph_dict = {"A": ["B", "C", "H"],
              "B": ["D", "G"],
              "C": ["D", "E"],
              "D": ["F"],
              "G": ["F"],
              "E": ["F"],
              "H": ["B"]
              }

my_graph = Graph(graph_dict=graph_dict)
print(my_graph)
print(my_graph.bfs_for_sssp("A", "F"))
