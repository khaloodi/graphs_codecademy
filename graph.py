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


grand_central = Vertex("Grand Central Station")

railway = Graph()

print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)
