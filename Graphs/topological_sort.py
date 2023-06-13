from collections import defaultdict

class Graph:

    def __init__(self, number_of_vertices):
        self.vertices = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def __str__(self):
        string = ""
        for v in self.vertices:
            string += f"{v}: {self.vertices[v]}\n"
        return string

    def add_edge(self, vertex, edge): # We are not adding vertex because the default dict will do that for us automatically
        self.vertices[vertex].append(edge)

    def topological_sort(self):

        def topological_sort_helper(visited, stack, current_vertex, vertices):
            visited.append(current_vertex)

            for edge in vertices[current_vertex]:
                if edge not in visited:
                    topological_sort_helper(visited, stack, edge, vertices)

            stack.append(current_vertex)

        visited = []
        stack = []
        for current_vertex in  list(self.vertices.keys()):
            if current_vertex not in visited:
                topological_sort_helper(visited, stack, current_vertex, self.vertices)

        while len(stack) > 0:
            print(stack.pop())

customGraph = Graph(8)
customGraph.add_edge("A", "C")
customGraph.add_edge("C", "E")
customGraph.add_edge("E", "H")
customGraph.add_edge("E", "F")
customGraph.add_edge("F", "G")
customGraph.add_edge("B", "D")
customGraph.add_edge("B", "C")
customGraph.add_edge("D", "F")
print(customGraph)
customGraph.topological_sort()