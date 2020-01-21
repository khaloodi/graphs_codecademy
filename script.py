# imports
from graph import Graph
from vertex import Vertex

# make the Graph instance
railway = Graph()

# create Vertex instances
station_one = Vertex("Chicago")
station_two = Vertex("Lake")

# call .add_vertex()
railway.add_vertex(station_one)
railway.add_vertex(station_two)

# call .add_edge()
railway.add_edge(station_one, station_two)
