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
    if current_vertex == target_value:
        return visited 

    # add recursive case 
    # loop through each neighbor of the current vertex in the graph:
    for neighbor in graph[current_vertex]:
        # if neighbor has not been visited:
        if neighbor not in visited:
        # recursively call dfs on neighbor
            path = dfs(graph, neighbor, target_value, visited)
            # if a path exists:
            if path:
            # return the path
                return path 
    return None 


the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
}

# Call dfs() below and print the result:
print(dfs(the_most_dangerous_graph, 'crocodiles', 'bees'))
