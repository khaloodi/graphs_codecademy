# imports
from graph import Graph
from vertex import Vertex


# make the Graph instance
railway = Graph()

# create Vertex instances
callan = Vertex('callan')
peel = Vertex('peel')
ulfstead = Vertex('ulfstead')
harwick = Vertex('harwick')

# call .add_vertex()
railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)

# call .add_edge()
railway.add_edge(peel, harwick)
railway.add_edge(harwick, callan)
railway.add_edge(callan, peel)

# Test it out
peel_to_ulfstead_path_exists = railway.find_path('peel', 'ulfstead')
harwick_to_peel_path_exists = railway.find_path('harwick', 'peel')

print("A path exists between peel and ulfstead:")
print(peel_to_ulfstead_path_exists)
print("A path exists between harwick and peel:")
print(harwick_to_peel_path_exists)