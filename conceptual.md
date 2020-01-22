# Graph Search Conceptual Review

There are three main traversal orders that you’ll come across for graph traversal:

- Preorder, in which each vertex is added to the “visited” list and added to the output list BEFORE getting added to the stack
- Postorder, in which each vertex is added to the “visited” list and added to the output list AFTER it is popped off the stack
- Reverse Post-Order (also known as Topological Sort), which returns an output list that is exactly the reverse of the post-order list

You’ve learned a bunch about graph searches and how to use them effectively:

- You can use a graph search algorithm to traverse the entirety of a graph data structure to locate a specific value
- Vertices in a graph search include a “visited” list to keep track of whether or not each vertex has been checked
- Depth-first search (DFS) and breadth-first search (BFS) are two common approaches to graph search
- The runtime for graph search algorithms is O(vertices + edges)
- DFS, which employs either recursion or a stack data structure, is useful for determining whether a path exists between two points
- BFS, which generally relies on a queue data structure, is helpful in finding the shortest path between two points
- There are three common traversal orders which you can apply with DFS to generate a list of all values in a graph: pre-order, post-order, and reverse post-order