"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {} # ensures that each node is cloned only once and helps to handle cycles

        def dfs(node):
            if not node:
                return

            # If the node has already been cloned, return the cloned node
            if node in cloned:
                return cloned[node]

            # Create a new node (clone) with the same value as the original node
            copy = Node(node.val)
            # Store the cloned node in the dictionary with the original node as the key
            cloned[node] = copy
            # Iterate over all the neighbors of the original node
            for nei in node.neighbors:
                # Recursively clone each neighbor and add it to the cloned node's neighbors list
                copy.neighbors.append(dfs(nei))
            # Return the cloned node
            return copy
        
        return dfs(node)
        