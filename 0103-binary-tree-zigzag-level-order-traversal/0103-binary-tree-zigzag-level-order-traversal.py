# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Use a queue to store all the nodes incrementally as we go
# we also store the level in our loop
# We make an alternating approach to how we are going to append the nodes to the queue
# lastly, we return the final res list
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return None
        
        queue = collections.deque()
        queue.append(root)
        
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            res.append(level)
            
        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()
        
        return res
                    
                    
                
            
        
        