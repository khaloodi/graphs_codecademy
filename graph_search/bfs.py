'''
Breadth-First Search: Take My Breadth Away
Unlike DFS, BFS is primarily concerned with the shortest path that exists between two points, so that’s what we’ll be thinking about as we build out our breadth-first search function.

Using a queue will help us keep track of the current vertex and its corresponding path. Unlike with DFS, with BFS we may have to expand on paths in several directions to find the path we’re looking for. Because of this, our path is not the same as our visited vertices.

For visited we don’t care about the order of visitation; we only care about whether a vertex is visited or not, so we’ll use a Python set. Our breadth-first search logic should begin something like this:

def bfs(graph, start_vertex, target_value):

  set path to a list containing the start_vertex

  create a queue to hold vertices and their corresponding paths

  define an empty visited set
'''


# def bfs(graph, start_vertex, target_value):
def bfs(graph, start_vertex, target_value):
    # set path to a list containing the start_vertex
    path = [start_vertex]
    # create a queue to hold vertices and their corresponding paths
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    # define an empty visited set
    visited = set()
