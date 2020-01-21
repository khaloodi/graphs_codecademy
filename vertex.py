class Vertex:
    def __init__(self, value):    
        self.value = value 
        self.edges = {}

    def add_edge(self, vertex):
        """
        Takes in a Vertex and adds an edge
        Ex: vertex.add_edge(vertex2) creates an edge
        b/w vertex one and vertex2
        """
        print('Adding edge to ' + vertex.value)
        self.edges[vertex.value] = True

    def get_edges(self):
        """
        Returns a list of the keys of the edges dictionary
        """
        return list(self.edges.keys())


# lake = Vertex("Lake")
# print(lake.get_edges())

# chicago = Vertex("Chicago")
# lake.add_edge(chicago)

# print(lake.get_edges(), chicago.get_edges())