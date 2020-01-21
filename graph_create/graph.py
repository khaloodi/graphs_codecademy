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
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        # Use a dictionary to track which
        # vertices we've already visited
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            # Update the `seen` variable
            # now that we've visited current_vertex
            seen[current_vertex] = True
            print("Visiting " + current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                
                # Filter next_vertices so it only
                # includes vertices NOT IN seen
                next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
                #next_vertices = [vertex for vertex in next_vertices ???????]
                start.extend(next_vertices)
        
        return False