# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addVal(s1, s2):
            int1, int2 = 0,0
            for i in s1:
                int1 = int1 * 10 + int(i)
            
            for i in s2:
                int2 = int2 * 10 + int(i)
            
            return str(int1 + int2)

        dummy = ListNode()
        tail = dummy
        
        s1, s2 = "",""
        cur1, cur2 = l1, l2

        while cur1:
            s1 += str(cur1.val)
            cur1 = cur1.next
        
        while cur2:
            s2 += str(cur2.val)
            cur2 = cur2.next
        
        res = addVal(s1, s2)

        for i in res:
            tail.next = ListNode(int(i))
            tail = tail.next
        
        return dummy.next
        

            
        
        