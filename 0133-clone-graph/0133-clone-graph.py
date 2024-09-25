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
        
        if not node:
            return None
        
        res = {}
        
        def dfs(clone):
            if clone and clone in res:
                return res[clone]
            
        
            copy = Node(clone.val)
            res[clone] = copy
            
            
            
            
            for i in clone.neighbors:
                copy.neighbors.append(dfs(i))
            
            return copy
                
            
        
        return dfs(node)
        
            


        

        