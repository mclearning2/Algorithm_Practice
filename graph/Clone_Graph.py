"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        clone = defaultdict()
        
        def dfs(node):
            if node in clone:
                return clone[node]
            
            clone_node = Node(node.val, [])
            clone[node] = clone_node
            
            for n in node.neighbors:
                clone_node.neighbors.append(dfs(n))
            
            return clone_node
        
        return dfs(node)