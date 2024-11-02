# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        cur = head
        length = 0
        node1, node2 = 0, 0

        while cur:
            length += 1
            if length == k:
                node1 = cur.val
            cur = cur.next
        
        cur = head
        count = 0

        while cur:
            count += 1
            if count == length - (k-1):
                node2 = cur.val
            cur = cur.next
        
        cur = head

        count = 0
        
        while cur:
            count +=1
            if count == k:
                cur.val = node2
            
            if count == length - (k -1):
                cur.val = node1
            
            cur = cur.next
        
        return head


        print(node1, node2) 


        