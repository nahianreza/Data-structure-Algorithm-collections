# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def addVal(newList):
            
            curr = newList
            res = 0
            while curr:
                res = res * 10 + curr.val
                curr = curr.next
            
            return res
        
        
        dummy = ListNode()
        tail = dummy
        
        
        sum1, sum2 = addVal(l1), addVal(l2)
        
        total = str(sum1 + sum2)
        
        for i in total:
            tail.next = ListNode(int(i))
            tail = tail.next
        
        return dummy.next
        
        
        
        
            
        
        