'''
A Graph Search with Real Depth
Let’s dig into our depth-first search function and consider: what do we actually want the algorithm to do for us?

- Find out if a path exists between vertices and return True or False accordingly?
- Return the distance between origin and destination that we get for the first path the function finds?
- Return the path itself? 
'''

'''
NOTE: We’ll go with the third option here, which gives us the other information as well.
The beginning of our depth-first function will look something like this:

def dfs(graph, current_vertex, target_value, visited):
  set visited to empty list if not yet set
  add current_vertex to visited
'''

def dfs(graph, current_vertex, target_value, visited=None):
    '''
    This is a recursive implimentation of DFS
    '''
    # set visited to empty list if not yet set
    if visited == None:
        visited = []
    # add current_vertex to visited
    visited.append(current_vertex)
    # build out base case, if the current vertex is the same 
    # as the value we are looking for, then, done searching, return our path (the visited list)
