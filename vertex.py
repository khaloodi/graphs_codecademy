class Vertex:
    def __init__(self, value):    
        self.value = value 
        self.edges = {}

    def get_edges(self):
        """
        Returns a list of the keys of the edges dictionary
        """
        return list(self.edges.keys())


station = Vertex("Cronk")
print(station.get_edges())