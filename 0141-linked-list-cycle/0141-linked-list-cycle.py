# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        curr = head
        visited_nodes = set()
        
        while curr:
            if curr in visited_nodes:
                return True
            visited_nodes.add(curr)
            
            curr = curr.next
            
        return False
            
            
        