# Bring in the Vertex class from vertex.py
from vertex import Vertex

"""
Our Graph class will track all the vertices and handle higher level concerns like whether the graph is directed, 
requiring edges to have a set direction, or undirected, allowing bi-directional movement across edges.
"""

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding " + vertex.value)
        self.graph_dict[vertex.value] = vertex 

    def add_edge(self, from_vertex, to_vertex):
        print("Adding edge from " + str(from_vertex.value) + " to " + str(to_vertex.value))
        self.graph_dict[from_vertex.value] = from_vertex.add_edge(to_vertex.value)

        if not self.directed:
            self.graph_dict[to_vertex.value] = to_vertex.add_edge(from_vertex.value)