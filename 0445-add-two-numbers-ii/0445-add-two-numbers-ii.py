# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addVal(l):
            res = 0
            while l:
                res = res * 10 + l.val
                l = l.next
            
            return res


        dummy = ListNode()
        tail = dummy
        
        
        total = str(addVal(l1) + addVal(l2))

        for i in total:
            tail.next = ListNode(int(i))
            tail = tail.next
        
        return dummy.next
        

            
        
        