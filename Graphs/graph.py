class Graph:
    def __init__(self, initial_vertices=None):
        self.vertices = {}
        if initial_vertices is not None:
            self.vertices = initial_vertices

    def __str__(self):
        string = ""
        for v in self.vertices:
            string += f"{v} : {self.vertices[v]}\n"
        return string

    def add_vertex(self, vertex):
        if vertex not in self.vertices.keys():
            self.vertices[vertex] = []
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.vertices.keys():
            for v in self.vertices:
                if vertex in self.vertices[v]:
                    self.vertices[v] = self.vertices[v].remove(vertex)
            self.vertices.pop(vertex)
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices.keys() and vertex2 in self.vertices.keys():
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices.keys() and vertex2 in self.vertices.keys():
            if vertex2 in self.vertices[vertex1]:
                self.vertices[vertex1].remove(vertex2)
            if vertex1 in self.vertices[vertex2]:
                self.vertices[vertex2].remove(vertex1)
            return True
        return False

    def bfs_traverse(self):
        start_vertex = next(iter(self.vertices.keys()))
        queue = [start_vertex]
        visited = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex)
                visited.append(vertex)
                for v in self.vertices[vertex]:
                    queue.append(v)

    def dfs_traverse(self):
        start_vertex = next(iter(self.vertices.keys()))
        stack = [start_vertex]
        visited = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.append(vertex)
                for v in self.vertices[vertex]:
                    stack.append(v)




my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
print(my_graph)
my_graph.remove_vertex("A")
print(my_graph)
my_graph.add_edge("A","B")
my_graph.add_edge("C","B")
my_graph.add_edge("D","B")
my_graph.add_edge("E","B")
my_graph.add_edge("D","C")
my_graph.add_edge("E","D")
print(my_graph)
my_graph.remove_edge("E","B")
print(my_graph)
my_graph.bfs_traverse()
print("___")
my_graph.dfs_traverse()

