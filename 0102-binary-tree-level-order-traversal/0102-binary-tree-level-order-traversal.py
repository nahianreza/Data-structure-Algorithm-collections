# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        newList = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            qlen = len(queue)
            level = []
            for i in range(qlen):
                newNode = queue.popleft()
                if newNode:
                    level.append(newNode.val)
                    queue.append(newNode.left)
                    queue.append(newNode.right)
            if level:
                newList.append(level)
        
        return newList




        