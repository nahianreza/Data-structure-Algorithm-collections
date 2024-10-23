"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = collections.deque()

        queue.append(root)

        root.next = None

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left and node.right:
                    node.left.next = node.right
                if node.left:
                    queue.append(node.left)      
                if node.right:
                    queue.append(node.right)

                cur = node.next
                while cur and not cur.left and not cur.right :
                    cur = cur.next
                
                if cur:
                    if cur.left and node.right:
                        node.right.next = cur.left
                    elif cur.left and node.left:
                        node.left.next = cur.left
                    elif cur.right and node.right:
                        node.right.next = cur.right
                    elif cur.right and node.left:
                        node.left.next = cur.right
        
        return root
                

                
                
        

            
                
                
        