# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseList(l):
            curr = l
            prev = None
            
            while curr:
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            
            return prev
        
        def addVal(reversedList):
            
            curr = reversedList
            res = 0
            while curr:
                res = res * 10 + curr.val
                curr = curr.next
            
            return res
        
        
        dummy = ListNode()
        tail = dummy
        
        reversedl1, reversedl2 = reverseList(l1), reverseList(l2)
        
        sum1, sum2 = addVal(reversedl1), addVal(reversedl2)
        total = str((sum1 + sum2))
        
        for i in total:
            tail.next = ListNode(int(i))
            tail = tail.next
            
        return reverseList(dummy.next)
    
    
        
        
                
        
                
        
        
            
        
        
        