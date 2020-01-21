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
        self.graph_dict[vertex.value] = vertex 

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)

        if not self.directed:
            self.graph_dict[to_vertex.value].to_vertex.add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        while len(start) > 0:
            current_vertex = start.pop(0)
            # current_vertex is end_vertex
            if current_vertex == end_vertex:
                # a path exists!
                return True
            # current_vertex is not end_vertex
            vertex = self.graph_dict[current_vertex]
            # add vertices connected to 
            next_vertices = vertex.get_edges()
            # current_vertex onto the list
            start.extend(next_vertices)
            # to keep searching for a path
            print("Visiting " + current_vertex)
        return False