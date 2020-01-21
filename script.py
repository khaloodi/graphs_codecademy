# imports
from graph import Graph
from vertex import Vertex

# make the Graph instance
railway = Graph()

# create Vertex instances
station_one = Vertex("Chicago")
station_two = Vertex("Lake")
station_three = Vertex("Grand")

# call .add_vertex()
railway.add_vertex(station_one)
railway.add_vertex(station_two)
railway.add_vertex(station_three)

# call .add_edge()
railway.add_edge(station_one, station_two, 3)
railway.add_edge(station_three, station_two, 5)
railway.add_edge(station_three, station_one)

print(station_one.edges)
print(station_three.edges)
print(station_two.edges)

railway.find_path(station_one, station_two)