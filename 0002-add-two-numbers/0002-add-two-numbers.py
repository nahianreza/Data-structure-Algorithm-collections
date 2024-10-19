# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseList(l):
            prev = None
            cur = l 

            while cur:
                after = cur.next
                cur.next = prev
                prev = cur
                cur = after
            
            return prev
        
        def addVal(list1):
            cur = list1
            res = 0

            while cur:
                res = res * 10 + cur.val
                cur = cur.next

            return res 



        
        l1, l2 = reverseList(l1), reverseList(l2)
        res = 0

        dummy = ListNode()
        tail = dummy

        sum1, sum2 = addVal(l1), addVal(l2)

        totalSum = str(sum1 + sum2)

        for i in range(len(totalSum)):
            tail.next = ListNode(int(totalSum[i]))
            tail = tail.next
        
        return reverseList(dummy.next)



    
    
        
        
                
        
                
        
        
            
        
        
        