class Vertex:
    def __init__(self, value):    
        self.value = value 
        self.edges = {}


    def add_edge(self, vertex):
        print('Adding edge to ' + vertex.value)
        self.edges[vertex.value] = True
        

    def get_edges(self):
        return list(self.edges.keys())

