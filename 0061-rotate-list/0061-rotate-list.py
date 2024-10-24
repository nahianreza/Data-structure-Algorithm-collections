# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail = head
        s = 1
        while tail.next:
            tail = tail.next
            s+= 1

        k = k % s
        if k == 0:
            return head
        
        
        breakPoint = s - k - 1
        cur = head

        for _ in range(breakPoint):
            cur = cur.next


        temp = cur.next
        cur.next = None

        tail.next = head

        
        return temp
        
        
            
            
        